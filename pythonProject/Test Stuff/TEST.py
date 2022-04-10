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

# time = datetime.now(tz=None)
#
# print(time)

time = datetime.timetuple(year)
for time_type in time:
    bruh = bruh + time_type
print(time)