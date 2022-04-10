import discord
#import random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

client = commands.Bot(command_prefix="d!")
slash = SlashCommand(client, sync_commands=True)

token = "OTM0MTk2NTUxODU5OTc0MTk1.YeskVg.T6tuw-NYsvqObh9Hku84qlrgHB8"


@slash.slash(
    name="Test",
    description="Gives you a list of commands for dan bot",
    guild_ids=[792290455752146954]
)
async def _hello(ctx:SlashContext):
    await ctx.send("Test")

client.run(token)