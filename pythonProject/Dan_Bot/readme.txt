figure out why did didnt work me



Currently Does Not Work Cuz Bot Code Was Leaked...
STEPS:

CHANGE THE BOT KEY
MAKE GIT IGNORE WORK
FREE SAILING

wrong
    async def btn1click(interaction: discord.Interaction):
        btn.disabled = True
        await interaction.response.edit_message(view=view)
        number6 = random.randrange(1,6)
        await interaction.followup.send(f'Your number is, {number6}')

right
    async def btn1click(interaction: discord.Interaction):
        btn.disabled = True
        await interaction.response.edit_message(view=view)
        number6 = random.randint(1, 6)
        await interaction.followup.send(f'Your number is, {number6}')

#Update: It was because one is random.randint and the other is random.randrange





DISCORD BOT IDEAS:
##### Make a calculator out of the discord buttons (Button commands)
      Make this calculator edit/update in real time so others see what ur doin

##### Figure out how dropdowns work and do ufnky stuff with em!

##### Funny image editor/edits (Using pillow rn)
##### Make it so that when u press a button, it scrolls between the image edits
##### Make it so that when u press a button, it changes what time the bot it gives you (Year, month, day)
##### Make it so you press a button, and it gives you permissions to use a certian command (Prob epic command)
##### Make it so when u press button it gets disables
##### Optimise the roll commend (Instead of "(1,2,3,4,5,6)", Make it custumisable. (Maybe with the option thing, black prompt thing, y know what im talkin about)
##### Fake Econemy or stock looker
#####

##### Make wordle, or tetris

###### Make cool web game, black background
###### white graphics only, with some cool exeptions. When something goes to edge of screen, it immediately (smoothly) teleports to opposite edge
###### Not really a game, but a thing to play around in i guess


Tips for me:

USEFUL VIDEO: https://www.youtube.com/watch?v=4CU0dm7rZ6o
GOOD PARTS: 19:40

https://www.youtube.com/watch?v=JeznW_7DlB0&list=PLY5Btrw0xVmuxOJmqIZMR8HcXDNIKYjOK&index=5
GOOD PARTS: 32:00~

USEFUL LINKS:

https://www.youtube.com/c/NeuralNine/videos - GO TO BOTTEM

https://easy-pil.readthedocs.io/en/latest/pages/intro.html

https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime




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