import json
import requests
import discord
from discord.ext import commands
import asyncio
import time
import subprocess
import os

desc = "Bot made by molchu and CodeWritten for a game called Hackers to make simple and complex calculations"

with open('botToken.txt', 'r') as f:
	TOKEN = f.read()

bot = commands.Bot(command_prefix = ".", description=desc)

@bot.event
async def on_ready():
    print("Up and running")

#the command below it a test command and adds no functions to the bot whatsoever
@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def listParameter(ctx programOrNode: str, parameter: str, level: str):
    with open("{}.json".format(programOrNode), "r") as f:
        temp1 = json.loads(f)
        temp2 = temp1[parameter]
        temp3 = temp2[level]
    await ctx.send("```{}```".format(temp3))
bot.run(TOKEN)
