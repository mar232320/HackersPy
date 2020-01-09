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
    try:
        with open("{}.json".format(argsList[0]), "r") as f:
            temp1 = json.load(f)
            temp2 = temp1[argsList[1]]
        if len(argsList) == 3:
            temp3 = temp2[argsList[2]]
            embed=discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url = temp1["imageAddress"])
            embed.add_field(name="Level " + str(argsList[2]) + " " + argsList[0] + ":" , value=str(temp3) + "", inline=True)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url = temp1["imageAddress"])
            if argsList[1] == "compilationPrice" or argsList[1] == "DPS" or argsList[1] == "firewall":
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
                        embed.add_field(name="Level " + str(name) + ":" , value=str(value) + " dmg", inline=True)
                    elif argsList[1].lower() == "firewall":
                        embed.add_field(name="Level " + str(name) + ":" , value=str(value) + " hp", inline=True)
                await ctx.send(embed=embed)
            else:
                if len(argsList) == 2:
                    embed.add_field(name=argsList[0].capitalize() + ":", value=str(temp2), inline=True)
                    await ctx.send(embed=embed)
    except:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Oops, something went wrong!",value="Either there's something mistyped or missing, or this probably is a bug. Contact CodeWritten#4044 or molchu#2575 if you think this is a bug.", inline = False)
        await ctx.send(embed=embed)
bot.run(TOKEN)
