from os import name
import discord
from discord import Option
from discord.ui import Button
from discord.ui import View
from discord import guild
from discord import colour
from discord import emoji
#from discord.commands.commands import option
from discord.ext import commands
from discord.components import SelectOption
from discord.commands import slash_command
from discord.gateway import DiscordClientWebSocketResponse

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="roll", description= "Rolls a dice up to a specefied number")
async def Dice_roll(ctx):
    btn = Button(
        label = "This is a button?",
        style=discord.ButtonStyle.success,
    )
    btn2 = Button(
        label="This is also a button???",
        style=discord.ButtonStyle.blurple,
    )
    btn3 = Button(
        label="This is epic",
        url="https://www.youtube.com/watch?v=X_8Nh5XfRw0",
    )
    view = View()
    view.add_item(btn)
    view.add_item(btn2)
    view.add_item(btn3)
    await ctx.respond("Does this work?", view=view)

@bot.slash_command(description="Tells you your own name", guild_ids=[792290455752146954])
async def say_my_name(ctx):
    await ctx.respond(f'Your name is {ctx.author}')


@bot.slash_command(guild_ids=[792290455752146954])
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run("OTM0MTk2NTUxODU5OTc0MTk1.YeskVg.T6tuw-NYsvqObh9Hku84qlrgHB8")
