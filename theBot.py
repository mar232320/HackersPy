import json
import requests
import discord
from discord.ext import commands
import asyncio
import time
import subprocess
import os

desc = ("Bot made by molchu and CodeWritten for a game called Hackers to make simple and complex calculations")

bot = commands.Bot(command_prefix = ".", description=desc)

with open('botToken.txt') as f:
    TOKEN = f.read()

@bot.event
async def on_ready():
    print("Up and running")

#the command below it a test command and adds no functions to the bot whatsoever
@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def listParameter(ctx, *, args):
    argsList = args.split(' ')
    with open("{}.json".format(argsList[0]), "r") as f:
        temp1 = json.load(f)
        temp2 = temp1[argsList[1]]
        try:
            temp3 = temp2[argsList[2]]
            embed=discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url = temp1["imageAddress"])
            embed.add_field(name="Level " + str(argsList[2]) + " " + argsList[0] + ":" , value=str(temp3) + "", inline=True)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url = temp1["imageAddress"])
            if argsList[1].lower() == "compilationprice" or "dps":
                for i in range(0,21):
                    a = []
                    b = []
                    for key in temp2.keys():
                        a.append(key)
                    for value in temp2.values():
                        b.append(value)
                    name = a[i]
                    value = b[i]
                    if argsList[1].lower() == "compilationprice":
                        embed.add_field(name="Level " + str(name) + ":" , value=str(value) + "B", inline=True)
                    elif argsList[1].lower() == "dps":
                        embed.add_field(name="Level " + str(name) + ":" , value=str(value) + "DPS", inline=True)
                await ctx.send(embed=embed)

bot.run(TOKEN)
