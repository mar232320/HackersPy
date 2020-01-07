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

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

bot.run(TOKEN)
