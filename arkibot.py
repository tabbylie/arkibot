import discord
from discord.ext import commands
from tabulate import tabulate
import random
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="//")

extensions = [
    "cogs.commands",
    "cogs.events",
    "cogs.embed"
]


@bot.command()
@commands.is_owner()
async def load(ctx, *extensionss):
    if extensionss:
        for extension in extensionss:
            try:
                bot.load_extension(f"cogs.{extension}")
                await ctx.send(f"{extension} has been loaded.")
            except Exception as e:
                await ctx.send(f"{extension} could not be loaded.")
                print(f"{extension} could not be loaded. [{e}]")
    else:
        for extension in extensions:
            try:
                bot.load_extension(extension)
                await ctx.send(f"{extension[5:]} has been loaded.")
            except Exception as e:
                await ctx.send(f"{extension[5:]} could not be loaded.")
                print(f"{extension[5:]} could not be loaded. [{e}]")


@bot.command()
@commands.is_owner()
async def unload(ctx, *extensionss):
    if extensionss:
        for extension in extensionss:
            try:
                bot.unload_extension(f"cogs.{extension}")
                await ctx.send(f"{extension} has been unloaded.")
            except Exception as e:
                await ctx.send(f"{extension} could not be unloaded.")
                print(f"{extension} could not be unloaded. [{e}]")
    else:
        for extension in extensions:
            try:
                bot.unload_extension(extension)
            except Exception as e:
                await ctx.send(f"{extension[5:]} could not be unloaded.")
                print(f"{extension[5:]} could not be unloaded. [{e}]")


@bot.command()
@commands.is_owner()
async def reload(ctx, *extensionss):
    if extensionss:
        for extension in extensionss:
            try:
                bot.reload_extension(f"cogs.{extension}")
                print(f"{extension} has been reloaded.")
                await ctx.send(f"{extension} has been reloaded.")
            except Exception as e:
                print(f"{extension} could not be reloaded. [{e}]")
                await ctx.send(f"{extension} could not be reloaded.")
    else:
        for extension in extensions:
            try:
                bot.reload_extension(extension)
                print(f"{extension[5:]} has been reloaded.")
                await ctx.send(f"{extension[5:]} has been reloaded.")
            except Exception as e:
                print(f"{extension[5:]} could not be reloaded. [{e}]")
                await ctx.send(f"{extension[5:]} could not be reloaded.")


@bot.command()
@commands.is_owner()
async def status(ctx):
    """
    Gives status for cogs.
    Array format:
    [
            ['cog', 'status'],
            ['cog', 'status']
    ]
    """
    statuses = []
    for extension in extensions:
        try:
            bot.load_extension(extension)
            statuses.append([extension[5:], "unloaded"])
            bot.unload_extension(extension)
        except commands.ExtensionAlreadyLoaded:
            statuses.append([extension[5:], "loaded"])
        except commands.ExtensionError:
            statuses.append([extension[5:], "error"])

    formatted_arr = tabulate(
        statuses, headers=["Cog", "Status"], tablefmt="pretty", colalign=("left",)
    )
    await ctx.send(f"`{formatted_arr}`")


@bot.command()
@commands.is_owner()
async def load_on(ctx):
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"{extension[5:]} could not be loaded. [{e}]")


@bot.command()
@commands.is_owner()
async def unload_off(ctx):
    for extension in extensions:
        try:
            bot.unload_extension(extension)
        except Exception as e:
            print(f"{extension[5:]} could not be unloaded. [{e}]")


@bot.command()
@commands.is_owner()
async def on(ctx):
    try:
        await ctx.invoke(bot.get_command("load_on"))
    except Exception as e:
        print(f"err {e}")

    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(
            "^help is fun I guess")
    )


@bot.command()
@commands.is_owner()
async def off(ctx):
    listed = ["Going to sleep", "zzz...", "Bye", "I can sleep again!"]
    listed = random.choice(listed)
    await ctx.send(f"{listed}")
    sleep(0.3)
    try:
        await ctx.invoke(bot.get_command("unload_off"))
    except Exception as e:
        print(f"err {e}")
    await bot.change_presence(status=discord.Status.invisible)


@bot.command()
@commands.is_owner()
async def full_off(ctx):
    listed = ["Going to sleep", "zzz...", "Bye", "I can sleep again!"]
    listed = random.choice(listed)
    await ctx.send(f"{listed}")
    sleep(0.3)
    await bot.logout()


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f"{extension[5:]} has been loaded.")
        except Exception as e:
            print(f"{extension[5:]} couldn't be loaded. [{e}]")

    bot.run(os.environ['SECRET_KEY'])
