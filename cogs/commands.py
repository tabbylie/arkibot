import discord
from discord.ext import commands
import subprocess
import sys
import os
import re
import random
from datetime import datetime, timedelta
from time import sleep
import json
import requests


class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx):
        hellu = ["Hello", "sup", "hi", "Good day",
                 "Why are you speaking to me?"]
        hellus = random.choice(hellu)
        await ctx.send(f"{hellus}")


def setup(bot):
    bot.add_cog(commands(bot))
