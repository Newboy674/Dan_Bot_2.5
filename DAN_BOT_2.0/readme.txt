

DISCORD BOT IDEAS: Make a calculator out of the discord buttons (Button commands)

Make it so you press a button, and it gives you permissions to use a certian command (Prob epic command)

Make it so when u press button it gets disables

Optimise the roll commend (Instead of "(1,2,3,4,5,6)", Make it custumisable. (Maybe with the option thing, black prompt thing, y know what im talkin about)

Tips for me:

Example:

@bot.slash_command(name="say_my_name_test", description="Tells you your own name", guild_ids=[792290455752146954])
async def say_my_name(ctx):

In that example, if i got rid of - name="say_my_name_test" -, it would default on as a discord command as
he def/function of say_my_name,
on the second line

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