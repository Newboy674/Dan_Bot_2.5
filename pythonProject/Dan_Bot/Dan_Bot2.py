from os import name
from datetime import datetime, date, time, timezone, tzinfo, timedelta
import discord
from discord import File
from discord import Option
from discord.ui import Button
from discord.ui import View
from discord import guild
from discord import colour
from discord import emoji
# from discord.commands.commands import option
from discord.ext import commands
from discord.components import SelectOption
from discord.commands import slash_command
from discord.gateway import DiscordClientWebSocketResponse
from easy_pil import Editor, Canvas, load_image_async
from Image_editor import Image_menu

import random
import python_weather

from discord.ext import tasks, commands

import datetime
import pytz



bot = discord.Bot()
DanImage = Image_menu()

guild_list = [672572967254753311, 792290455752146954]

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@tasks.loop(time = datetime.time(15,45,0,0,tzinfo=pytz.timezone("America/Los_Angeles")))
async def sendmessage(ctx):
    print("buh")
    await ctx.send("sent at the set time im too lazy to specify")

@bot.slash_command(name="test", description="sussy baka", guild_ids = guild_list)
async def loop(ctx):

    current = datetime.datetime.now(tz=pytz.timezone("America/Los_Angeles"))
    test = datetime.time(15,45,0,0,tzinfo= (pytz.timezone("America/Los_Angeles")))
    new_line = "\n"
    await ctx.respond(f'Loop Begin! {new_line} It is currently: {current} {new_line} And a message *should* appear at: {test}')
    sendmessage.start(ctx)

# import schedule
# import time
# @bot.loop
# async def cum():
#     def timed_link():
#         print(f"minute")
#     print(f"test")
#     schedule.every(1).minutes.do(timed_link)
#     schedule.run_pending()


# @bot.slash_command(name="timeset", description="Sets the time zone for the time command",guild_ids=[792290455752146954])

#@bot.slash_Command(name="Roman Converter", description="Give it roman numbers", guild_ids=[792290455752146954])



# @bot.slash_command(name="time", description="gives the time, based off of the time zone set command", guild_ids=[792290455752146954])
# async def time(ctx):
#     if timezone = 0
#        time = datetime.now(tz=none)
#
#     await ctx.respond(time)






@bot.slash_command(name="your_avatar", description="Should post an image of your avatar", guild_ids=guild_list)

async def your_avatar(ctx):
    profile = await load_image_async(ctx.author.display_avatar.url)
    editor = Editor(profile).circle_image()
    editor = Editor(profile).resize([200, 200],crop=True)
    file = File(fp=editor.image_bytes, filename='imagine reading this lol.png')
    await ctx.respond("Work pls")
    await ctx.send(file=file)





@bot.slash_command(name="roll_dice", description="Rolls a dice up to a specefied number",     guild_ids=guild_list)

async def Dice_roll(ctx):
    # Button formatting below
    btn1 = Button(
        label="Roll up to 6",
        style=discord.ButtonStyle.blurple,
    )
    btn2 = Button(
        label="Roll up to 20",
        style=discord.ButtonStyle.red,
    )
    btn3 = Button(
        label="Custom",
        style=discord.ButtonStyle.success,
    )
    view = View()
    view.add_item(btn1)
    view.add_item(btn2)
    view.add_item(btn3)

    # Stuff below is for button to be clickable
    # Can be named whatever
    #         l
    #         v
    async def btn1click(interaction: discord.Interaction): #On click, do the following...
        btn1.disabled = True
        btn2.disabled = True # To disable buttons
        btn3.disabled = True
        await interaction.response.edit_message(view=view)
        number_roll6 = random.randrange(1, 6)
        await interaction.followup.send(f'The 6 Dice Rolled, {number_roll6}')

    async def btn2click(interaction: discord.Interaction):
        btn1.disabled = True
        btn2.disabled = True  # To disable buttons
        btn3.disabled = True

        await interaction.response.edit_message(view=view)  # Also to disable button (Neccecary!!!)
        number20 = random.randrange(1, 20)
        await interaction.followup.send(f'The 20 Dice Rolled, {number20}')  # Use followup if you edit a message

    async def btn3click(interaction: discord.Interaction):
        btn1.disabled = True
        btn2.disabled = True
        btn3.disabled = True                                 # Disables button
        await interaction.response.edit_message(view=view)   # updates that the button was disabled on dcord
        await interaction.delete_original_message()
        await ctx.respond("Use the /cust command")



    btn1.callback = btn1click  # Assigns the button varible to the button click callback (makes button allign with correct click function)
    btn2.callback = btn2click
    btn3.callback = btn3click

    await ctx.respond("Choose a numba?", view=view)

@bot.slash_command(name="cust", description="Gives you the opportunity of a lifetime", guild_ids=guild_list)
async def Cust(ctx: discord.ApplicationContext,
                        min_val: Option(int, "Minimum value"),
                        max_val: Option(int, "Minimum value")
                        ):

    if min_val < max_val:
        number_random = random.randrange(min_val, max_val)
        await ctx.respond(f'Your random number, from {min_val} to {max_val}, is {number_random}')
    else:
        await ctx.respond(f'no')



@bot.slash_command(name="epicbutton", description="Gives you the opportunity of a lifetime", guild_ids=guild_list)
async def epicbutton(ctx):  # Just print this and ill understand what each part does
    btn4 = Button(
        label="The Epic Button",
        url="https://www.youtube.com/watch?v=X_8Nh5XfRw0",
    )
    view = View()
    view.add_item(btn4)

    embed = discord.Embed(
        title="THE EPIC BUTTON",
        description="PRESS THIS AND EPIC WILL HAPPEN!!!",
        color=discord.Color.dark_gold()
    )
    # Stuff below is formatting - not neccecary for button to work
    embed.set_author(name="Epic Button")
    embed.set_footer(text="Its very epic I promise")
    embed.set_thumbnail(
        url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fc.tenor.com%2Fhdl1-Mdo5XkAAAAC%2Fneko-arc.gif&imgrefurl=https%3A%2F%2Ftenor.com%2Fview%2Fneko-arc-gif-23482517&tbnid=gjiffNqQYFKmhM&vet=12ahUKEwjK1q_s4Mj1AhVPrHIEHUe_D3gQMygGegUIARDKAQ..i&docid=Va38oRCi6_dTWM&w=465&h=498&itg=1&q=neko%20arc&client=opera&ved=2ahUKEwjK1q_s4Mj1AhVPrHIEHUe_D3gQMygGegUIARDKAQ")
    embed.set_image(
        url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6830ce29-acc6-4e8d-8a49-04dec20f2750/d10mkhp-e8cea004-1bf2-42e7-a4da-c8632f7b4706.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzY4MzBjZTI5LWFjYzYtNGU4ZC04YTQ5LTA0ZGVjMjBmMjc1MFwvZDEwbWtocC1lOGNlYTAwNC0xYmYyLTQyZTctYTRkYS1jODYzMmY3YjQ3MDYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.XCSBRMJLfKOU97fzV9M_rHhT-Q5FdCWxgT-2EvtiEoo")
    # Stuff above is formatting
    await ctx.respond("EPIC BUTTON BELOW!!!", view=view, embed=embed)


@bot.slash_command(name="say_my_name_test", description="Tells you your own name", guild_ids=guild_list)
async def say_my_name(ctx):
    await ctx.respond(f'Your name is {ctx.author}')


@bot.slash_command(guild_ids=guild_list)
async def hello(ctx):
    await ctx.respond("World!")

@bot.slash_command(name="everyone", description="annoying", guild_ids=guild_list)
async def everyone(ctx):
    await ctx.respond()

@bot.slash_command(name="getweather", description="Tells you the weather",guild_ids=guild_list)
async def getweather(ctx):
    client = python_weather.Client(format=python_weather.METRIC)  ##makes the client & sets format setting
    weather = await client.find("London ON")                       ##Gives the client its location
    temp = weather.current.temperature
    if temp == 1 or temp == -1:
         await ctx.respond(f'The weather in London Ontario is probably {temp}° C')
    else:
        await ctx.respond (f'The weather in London Ontario is probably {temp}° C')

    await client.close()

bot.run("OTM0MTk2NTUxODU5OTc0MTk1.YeskVg.T6tuw-NYsvqObh9Hku84qlrgHB8")



##IDEA: make bot put in vc the "its 10:49" meme