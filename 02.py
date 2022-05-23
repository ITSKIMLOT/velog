import discord
from discord.ext import commands

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=INTENTS)
bot.remove_command(help)
token = "토큰을 붙혀넣으세요!" # 메시지를 지우고, 본인의 토큰을 넣어주세요.

@bot.event
async def on_ready(): # 봇의 준비를 감지합니다.
	print("봇이 준비되었습니다!")

bot.run(token) # 봇을 실행시킵니다.