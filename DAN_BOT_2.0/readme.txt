

DISCORD BOT IDEAS: Make a calculator out of the discord buttons (Button commands)



IGNORE MOST STUFF BELOW BECAUSE OF THIS YOUTUBE VIDEO: https://www.youtube.com/watch?v=4CU0dm7rZ6o






TAKEN FROM HERE: https://github.com/Pycord-Development/pycord/blob/master/README.rst

Examples of a / command

import discord

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run("token")

#################################################################

EXAMPLES OF A NORMAL COMMAND (WILL BE DISCONTINUED)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run("token")