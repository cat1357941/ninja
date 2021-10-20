import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = '=')

@bot.command()

async def 金鑰匙單抽(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)





bot.run("OTAwMTExNzA3ODE5NjA2MDY2.YW8kWg.Ej48HiXn8TLGIuOrbSdPYtXnVcU")

