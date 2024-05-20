import discord
import time
import os
import videogen

intents = discord.Intents.default()
intents.message_content = True

from dotenv import load_dotenv
from discord.ext import commands
from checks import is_owner

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


bot = commands.Bot(command_prefix="?", intents=intents)

async def load_cogs(bot):
    cogs = [videogen]
    for cog in cogs:
        if not bot.get_cog(cog.__name__):
            try:
                await bot.load_extension(cog.__name__)
            except Exception as e:
                print(f"Failed to load cog {cog.__name__}: {e}")

@bot.command(pass_context=True, hidden=True)
@commands.check(is_owner)
async def sync(ctx):
    await ctx.bot.tree.sync()
    await ctx.send("Commands synced, you will need to reload Discord to see them")
    await ctx.message.delete()

@bot.command()
@commands.check(is_owner)
async def list_cogs(ctx):
    loaded_cogs = "\n".join(bot.cogs.keys())
    await ctx.send(f"Loaded cogs: \n{loaded_cogs}")
    await ctx.message.delete()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("Ready")

@bot.event
async def on_connect():
    print("Bot is starting")
    await load_cogs(bot)
    print("Setup complete")



bot.run(TOKEN)
