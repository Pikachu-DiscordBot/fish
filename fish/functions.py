from datetime import datetime
from typing import List
import discord
from redbot.core.utils import AsyncIter

def check_weekend():
    return True #if datetime.today().weekday() in [4, 5, 6] else False

async def get_leaderboard(self, guild: discord.Guild = None) -> List[tuple]:
    raw_accounts = await self.config.all_users()
    if guild is not None:
        tmp = raw_accounts.copy()
        for acc in tmp:
            if not guild.get_member(acc):
                del raw_accounts[acc]
    a = []
    async for (k, v) in AsyncIter(raw_accounts.items(), steps=100):
        lsum, rsu, usum, csum, gsum = (
            sum(v["legendary"].values()),
            sum(v["rare"].values()),
            sum(v["uncommon"].values()),
            sum(v["common"].values()),
            sum(v["garbage"].values()),
        )
        _sum = lsum + rsu + usum + csum + gsum
        a.append((k, {"fishes": _sum, "legendaries": lsum}))
    sorted_acc = sorted(
        a,
        key=lambda x: x[1]["fishes"],
        reverse=True,
    )
    return sorted_acc