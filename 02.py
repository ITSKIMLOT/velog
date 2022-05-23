import discord
from discord.ext import commands

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=INTENTS)
bot.remove_command(help)
token = "OTc3NTkwMzE3MjE5OTc5MzI1.GSvOAT.Hm8Wz9uXP0MwHjtBgP_PUbtkvo5xSMz6z6cPMU"

@bot.event
async def on_ready():
	print("봇이 준비되었습니다!")

bot.run(token)