
## W I P!!!


from os import name
import discord
from discord import File
from discord import Option
from discord.ui import Button
from discord.ui import View
from discord import guild
from discord import colour
from discord import emoji
#from discord.commands.commands import option
from discord.ext import commands
from discord.components import SelectOption
from datetime import datetime, date, time, timezone
from discord.commands import slash_command
from discord.gateway import DiscordClientWebSocketResponse
from easy_pil import Editor, Canvas, load_image_async

bot = discord.Bot()




class Image_menu:
    def __init__(self):
         async def preset_image(self,ctx):


                profile = await load_image_async(ctx.author.display_avatar.url)
                editor = Editor(profile).circle_image()
                editor = Editor(profile).resize([200,200],crop=True)    #Help from ---  https://easy-pil.readthedocs.io/en/latest/easy_pil/easy_pil.editor.html
                file = File(fp=editor.image_bytes, filename='imagine reading this lol.png')
                return file



    # def print_account(self):
    #         canvas = Canvas(width=500, height=500)
    #
    #         editor = Editor(canvas)
    #         editor.rectangle((50,50),50,50)
#editor.show()
