import logging
from typing import Dict, List, Tuple

import discord
from redbot.core.i18n import Translator
from redbot.core.utils.chat_formatting import escape, humanize_number
from redbot.vendored.discord.ext import menus

_ = Translator("Adventure", __file__)
log = logging.getLogger("red.cogs.adventure.menus")


class LeaderboardSource(menus.ListPageSource):
    def __init__(self, entries: List[Tuple[int, Dict]]):
        super().__init__(entries, per_page=10)

    def is_paginating(self):
        return True

    async def format_page(self, menu: menus.MenuPages, entries: List[Tuple[int, Dict]]):
        ctx = menu.ctx
        fish_len = len(humanize_number(entries[0][1]["fishes"]))
        start_position = (menu.current_page * self.per_page) + 1
        pos_len = len(str(start_position + 9)) + 2
        fish_len = (len("Fish") if len("Fish") > fish_len else fish_len) + 2
        legendary_len = len("Legendaries") + 2
        header = (
            f"{'#':{pos_len}}{'Fish':{fish_len}}"
            f"{'Legendaries':{legendary_len}}{'User':2}"
        )
        author = ctx.author

        if getattr(ctx, "guild", None):
            guild = ctx.guild
        else:
            guild = None

        players = []
        for position, acc in enumerate(entries, start=start_position):
            user_id = acc[0]
            account_data = acc[1]
            if guild is not None:
                member = guild.get_member(user_id)
            else:
                member = None

            if member is not None:
                username = member.display_name
            else:
                user = menu.ctx.bot.get_user(user_id)
                if user is None:
                    username = f"{user_id}"
                else:
                    username = user.name
            username = escape(username, formatting=True)

            if user_id == author.id:
                # Highlight the author's position
                username = f"<<{username}>>"

            pos_str = position
            fishes = humanize_number(account_data["fishes"])
            legendaries = humanize_number(account_data["legendaries"])
            data = (
                f"{f'{pos_str}.':{pos_len}}"
                f"{fishes:{fish_len}}"
                f"{legendaries:{legendary_len}}"
                f"{username}"
            )

            players.append(data)

        embed = discord.Embed(
            title="Fish Leaderboard",
            color=await menu.ctx.embed_color(),
            description="```md\n{}``` ```md\n{}```".format(
                header,
                "\n".join(players),
            ),
        )
        embed.set_footer(text=f"Page {menu.current_page + 1}/{self.get_max_pages()}")
        return embed
