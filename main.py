
import discord
import random
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет Я бот!{bot.user}')

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
    await ctx.send('{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def minus(ctx, left: int, right: int):
    """minus"""
    await ctx.send(left - right)
@bot.command()
async def x(ctx, left: int, right: int):
    "X"
    await ctx.send(left * right)
@bot.command()
async def divide(ctx, left: int, right: int):
    "/"
    await  ctx.send(left / right)
@bot.command()
async def rc(ctx):
    rcl = random.randint(1,100)
    await ctx.send(rcl)
@bot.command()
async def helps(ctx):
    await ctx.send("команда x умножает два числа команда divide делит два числа команда add плюсует два числа команда minus минусует два числа команда choose выбирает из разных строк команда rc выбирает рандомное число от 1 до 100")
    

bot.run("ващ токен тут")

