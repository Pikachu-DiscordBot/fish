import asyncio
import random
from datetime import date
from typing import Literal

import discord
import tabulate
from redbot.core import Config, bank, commands
from redbot.core.errors import BalanceTooHigh
from redbot.core.utils._dpy_menus_utils import (
    SimpleHybridMenu,
)  # WARNING: Wont work on normal current red version
from redbot.core.utils.chat_formatting import box, humanize_number
from redbot.core.utils.predicates import MessagePredicate

from .constants import *
from .functions import check_weekend, get_leaderboard
from .menus import LeaderboardSource


class Fish(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.config = Config.get_conf(self, 1398467138476, force_registration=True)
        self.config.register_user(
            legendary={"\N{DRAGON}": 0},
            epic={
                "\N{SHARK}": 0,
                "\N{SPOUTING WHALE}": 0,
            },
            rare={
                "\N{SQUID}": 0,
                "\N{OCTOPUS}": 0,
                "\N{DOLPHIN}": 0,
            },
            uncommon={
                "\N{TROPICAL FISH}": 0,
                "\N{BLOWFISH}": 0,
                "\N{LOBSTER}": 0,
            },
            common={
                "\N{FISH}": 0,
                "\N{SHRIMP}": 0,
                "\N{CRAB}": 0,
            },
            garbage={
                "\N{BATTERY}": 0,
                "\N{SHOPPING TROLLEY}": 0,
                "\N{MANS SHOE}": 0,
                "\N{WRENCH}": 0,
                "\N{BABY BOTTLE}": 0,
            },
            rod="wooden rod",
            all_rods={
                "wooden rod": 1,
                "magnet rod": 0,
                "fly-fishing rod": 0,
                "spinning rod": 0,
                "harpoon": 0,
                "telescopic rod": 0,
                "carbon-fibre rod": 0,
                "metal rod": 0,
                "trusty rod": 0,
                "pikachu rod": 0,
            },
        )

    @commands.group(invoke_without_command=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def fish(self, ctx):
        """Go fishing."""
        if ctx.assume_yes:
            return await ctx.send("You think you can trick me? Nice try.")
        if not await bank.can_spend(ctx.author, 10):
            return await ctx.send("You can't afford to cast out your line!")

        if random.randint(1, 100) == 100:
            a = random.randint(200, 490)
            if await bank.can_spend(ctx.author, a):
                await ctx.send(
                    random.choice(EVENTS).format(
                        amount=a, currency=await bank.get_currency_name(guild=ctx.guild)
                    )
                )
                await bank.withdraw_credits(ctx.author, a)
            else:
                await bank.set_balance(ctx.author, 0)
                event = random.choice(EVENTS).format(
                    amount=a, currency=await bank.get_currency_name(guild=ctx.guild)
                )
                event += "\nYou didn't have enough to pay off the remaining balance and are now bankrupt."
                await ctx.send(event)
            return
        await bank.withdraw_credits(ctx.author, 10)
        if random.randint(1, 350) == 350:
            animal = random.choice(["\N{SHARK}", "\N{SPOUTING WHALE}"])
            a = f"{ctx.author.display_name} pays 10 {await bank.get_currency_name(guild=ctx.guild)} to cast out their line.\n{ROD} **|** You caught a {animal}"
            msg = await ctx.send(a)
            await asyncio.sleep(2)
            a += "\nThe fish managed to escape."
            await msg.edit(content=a)
            return
        rod = await self.config.user(ctx.author).rod()
        if random.choices([1, 2], weights=[0.965, 0.035], k=1)[0] == 2:
            new_rod = random.choices(RODS, weights=RODS_WEIGHT, k=1)[0]
            await ctx.send(
                f"{ctx.author.display_name} pays 10 {await bank.get_currency_name(guild=ctx.guild)} to cast out their line.\n{ROD} **|** You feel a tug on the line and reel it in. You have found a new {new_rod}!"
            )
            async with self.config.user(ctx.author).all_rods() as rods:
                rods[new_rod.lower()] += 1
            return

        a = date.today().strftime("%d")
        state = random.getstate()
        random.seed(a)
        weather = random.choice(WEATHER_EFFECTS)
        random.setstate(state)
        if check_weekend():
            weights = WEIGHTS_WEEKEND(weather)
        else:
            weights = WEIGHTS(weather)

        fish = random.choices(FISHES, weights=weights[rod], k=1)[0]
        msg = await ctx.send(
            f"{ctx.author.display_name} pays 10 {await bank.get_currency_name(guild=ctx.guild)} to cast out their line on their {rod.title()} on a {weather} day.\n{ROD} **|** You caught a {fish}"
        )
        fish_type = FISHES_TYPE[fish]
        await self.deposit_fish(ctx.author, fish_type, fish)

    @fish.command(name="rods")
    async def fish_rods(self, ctx):
        """View your collection of rods."""
        conf = await self.config.user(ctx.author).all_rods()
        embed = discord.Embed(
            title=f"{ctx.author.name}'s rods", color=await ctx.embed_colour()
        )
        data = []
        for rod in RODS:
            if conf[rod] > 0:
                data.append([rod.title(), conf[rod]])
        embed.description = box(
            tabulate.tabulate(data, headers=["Rods", "Amount"]), lang="prolog"
        )
        await ctx.send(embed=embed)

    @fish.command(name="info")
    async def fish_info(self, ctx):
        """View your current fishing loadout."""
        rod = await self.config.user(ctx.author).rod()
        await ctx.send(f"Your current rod is a {rod.title()}.")

    @fish.command(name="select")
    async def fish_rodselect(self, ctx, *, rod: str):
        """Select your current rod."""
        conf = await self.config.user(ctx.author).all_rods()
        if rod.lower() not in conf:
            return await ctx.send("No such rod exists.")
        if conf[rod.lower()] > 0:
            await ctx.send(f"You have selected {rod.title()} as your current rod.")
            await self.config.user(ctx.author).rod.set(rod.lower())
        else:
            await ctx.send("You dont have any of those rods.")

    @fish.command(name="view", aliases=["list"])
    async def fish_view(self, ctx):
        """View your collection of fishes."""
        conf = await self.config.user(ctx.author).all()
        embed = discord.Embed(
            title=f"{ctx.author.name}'s fishes", color=await ctx.embed_colour()
        )
        for fish_type in conf:
            if fish_type not in ["legendary", "rare", "uncommon", "common", "garbage"]:
                continue
            msg = ""
            for fish in conf[fish_type]:
                if fish in FISHES:
                    if conf[fish_type][fish] > 0:
                        msg += f"{fish} - {conf[fish_type][fish]}\n"
            if msg:
                embed.add_field(name=fish_type.title(), value=msg)
        await ctx.send(embed=embed)

    @fish.command(name="sell")
    async def fish_sell(self, ctx, type: str):
        """Sell a type of fishes."""
        type = type.lower()
        if type not in ["legendary", "epic", "rare", "common", "uncommon", "garbage", "all"]:
            return await ctx.send(
                "That isn't a valid type. Valid types are legendary, rare, uncommon, common, garbage and all."
            )
        if type == "legendary":
            conf = await self.config.user(ctx.author).legendary()
            _sum = sum(conf.values())
            if _sum == 0:
                await ctx.send(
                    f"You claim to have legendary fish but you dont, the shop keeper fines you 150 {await bank.get_currency_name(ctx.guild)} for wasting his time."
                )
                if not await bank.can_spend(ctx.author, 150):
                    await bank.set_balance(ctx.author, 0)
                else:
                    await bank.withdraw_credits(ctx.author, 150)
                return
            cash = _sum * LEGENDARY_PRICE
            await self.config.user(ctx.author).legendary.clear()
            await self.sell_fishes(
                ctx, "legendary" if _sum == 1 else "legendaries", cash, _sum
            )
        elif type == "rare":
            conf = await self.config.user(ctx.author).rare()
            _sum = sum(conf.values())
            if _sum == 0:
                return await ctx.send(
                    "You don't have anything to sell, stop wasting the shopkeepers time."
                )
            cash = _sum * RARE_PRICE
            await self.config.user(ctx.author).rare.clear()
            await self.sell_fishes(ctx, "rare", cash, _sum)
        elif type == "uncommon":
            conf = await self.config.user(ctx.author).uncommon()
            _sum = sum(conf.values())
            if _sum == 0:
                return await ctx.send(
                    "You don't have anything to sell, stop wasting the shopkeepers time."
                )
            cash = _sum * UNCOMMON_PRICE
            await self.config.user(ctx.author).uncommon.clear()
            await self.sell_fishes(ctx, "uncommon", cash, _sum)
        elif type == "common":
            conf = await self.config.user(ctx.author).common()
            _sum = sum(conf.values())
            if _sum == 0:
                return await ctx.send(
                    "You don't have anything to sell, stop wasting the shopkeepers time."
                )
            cash = _sum * COMMON_PRICE
            await self.config.user(ctx.author).common.clear()
            await self.sell_fishes(ctx, "common", cash, _sum)
        elif type == "garbage":
            conf = await self.config.user(ctx.author).garbage()
            _sum = sum(conf.values())
            if _sum == 0:
                return await ctx.send(
                    "You don't have anything to sell, stop wasting the shopkeepers time."
                )
            cash = _sum * GARBAGE_PRICE
            await self.config.user(ctx.author).garbage.clear()
            await self.sell_fishes(ctx, "garbage", cash, _sum)
        elif type == "all":
            conf = await self.config.user(ctx.author).all()
            lsum, rsu, usum, csum, gsum = (
                sum(conf["legendary"].values()),
                sum(conf["rare"].values()),
                sum(conf["uncommon"].values()),
                sum(conf["common"].values()),
                sum(conf["garbage"].values()),
            )
            _sum = lsum + rsu + usum + csum + gsum
            if _sum == 0:
                return await ctx.send(
                    "You don't have anything to sell, stop wasting the shopkeepers time."
                )
            cash = (
                (lsum * LEGENDARY_PRICE)
                + (rsu * RARE_PRICE)
                + (usum * UNCOMMON_PRICE)
                + (csum * COMMON_PRICE)
                + (gsum * GARBAGE_PRICE)
            )
            await self.config.user(ctx.author).garbage.clear()
            await self.config.user(ctx.author).common.clear()
            await self.config.user(ctx.author).uncommon.clear()
            await self.config.user(ctx.author).rare.clear()
            await self.config.user(ctx.author).epic.clear()
            await self.config.user(ctx.author).legendary.clear()
            await self.sell_fishes(ctx, "all", cash, _sum)

    async def sell_fishes(self, ctx, type, amount, sum):
        try:
            await bank.deposit_credits(ctx.author, amount)
            await ctx.send(
                f"You've sold {sum}{'' if type == 'all' else f' {type}'} {'fish' if type not in ['garbage', 'all'] else 'item' if sum == 1 else 'items'} for {humanize_number(amount)} {await bank.get_currency_name(ctx.guild)}."
            )
        except BalanceTooHigh as e:
            await bank.set_balance(ctx.author, e.max_balance)
            await ctx.send(
                f"You've sold {sum}{'' if type == 'all' else f' {type}'} {'fish' if type not in ['garbage', 'all']  else 'item' if sum == 1 else 'items'} however you have reached the max balance so you must spend some more."
            )

    async def deposit_fish(
        self,
        user: discord.Member,
        _type: Literal["legendary", "rare", "uncommon", "common", "garbage"],
        fish: str,
    ):
        if _type == "legendary":
            fishes = await self.config.user(user).legendary()
            fishes[fish] += 1
            await self.config.user(user).legendary.set(fishes)
        elif _type == "rare":
            fishes = await self.config.user(user).rare()
            fishes[fish] += 1
            await self.config.user(user).rare.set(fishes)
        elif _type == "uncommon":
            fishes = await self.config.user(user).uncommon()
            fishes[fish] += 1
            await self.config.user(user).uncommon.set(fishes)
        elif _type == "common":
            fishes = await self.config.user(user).common()
            fishes[fish] += 1
            await self.config.user(user).common.set(fishes)
        elif _type == "garbage":
            fishes = await self.config.user(user).garbage()
            fishes[fish] += 1
            await self.config.user(user).garbage.set(fishes)

    @fish.command(name="leaderboard", aliases=["lb"])
    async def fish_leaderboard(self, ctx, global_users=False):
        """Fish Leaderboard"""
        data = await get_leaderboard(ctx.guild if not global_users else None)
        await SimpleHybridMenu(
            source=LeaderboardSource(data),
            cog=self,
            delete_message_after=True,
        ).start(ctx=ctx, wait=False)

    @commands.is_owner()
    @commands.command()
    async def fishsim(self, ctx, amount: int, rod):
        """."""
        msg = ""
        a = {k: 0 for k in FISHES}
        for weather in WEATHER_EFFECTS:
            weights = WEIGHTS(weather)
            for _ in range(amount):
                fish = random.choices(FISHES, weights=weights[rod], k=1)[0]
                a[fish] += 1
            for fish in a:
                a[fish] = round(a[fish] / amount * 100, 3)
            msg = f"{rod} - {weather} - {a}"
            await ctx.send(msg)

    @commands.group()
    async def fishshop(self, ctx):
        """Buy and sell your fishing needs."""

    @fishshop.command(name="buy")
    async def shop_buy(self, ctx, *, item=None):
        """Buy your fishing needs."""
        if item is None:
            data = [
                [rod.title(), humanize_number(RODS_PRICES[rod])] for rod in RODS[1:]
            ]
            embed = discord.Embed(
                title="Rod Prices",
                description=box(
                    tabulate.tabulate(data, headers=["Rod", "Price"]), lang="prolog"
                ),
                color=await ctx.embed_colour(),
            )
            await ctx.send(embed=embed)
            return
        if item not in RODS[1:]:  # Will eventually have more options.
            await ctx.send("No such item exists.")
            return
        price = RODS_PRICES[item]
        if not await bank.can_spend(ctx.author, price):
            return await ctx.send("You cannot afford that item.")
        msg = ""
        if check_weekend():
            msg += "The shopkeeper offers your a weekend discount of 10%\n"
            price = price * 0.90
        msg += f"Are you sure you want to spend {humanize_number(price)} {await bank.get_currency_name(ctx.guild)} on a {item.title()}?"
        await ctx.send(msg)
        try:
            pred = MessagePredicate.yes_or_no(ctx, user=ctx.author)
            await ctx.bot.wait_for("message", check=pred, timeout=20)
        except asyncio.TimeoutError:
            await ctx.send("You left the shop without purchasing anything.")
            return
        if not pred.result:
            await ctx.send(
                "Alright then, you leave the shop without purchasing anything."
            )
            return
        await bank.withdraw_credits(ctx.author, price)
        async with self.config.user(ctx.author).all_rods() as rods:
            rods[item.lower()] += 1
        await ctx.send(f"Congratulations on your new purchase of a {item.title()}!")

    # @fishshop.command(name="sell")
    # async def fish_sell(self, ctx, *, item):
    #     """Sell your unused fishing goods"""
    #     pass
