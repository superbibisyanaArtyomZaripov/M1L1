import discord
import random
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')




bot.run("MTIxNDIwODcyMzEwNzQ1NDk4Ng.GPwm-6.BNKDDl6YkQjkMohzTJK1i8nvKRaEgA0T4-QIIY")

