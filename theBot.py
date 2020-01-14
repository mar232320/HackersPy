import json
import requests
import discord
from discord.ext import commands
import asyncio
import time
import subprocess
import os

async def timeCal(progDamage,progInstallTime,progHitInterval,progProjectileTime,nodeFirewall,nodeRegeneration):
    time = 0
    i = 0
    stunnedTime = 2
    startshoot = -10000
    while True:
        if progDamage * 3.5 < nodeFirewall / 100 * nodeRegeneration:   
            i += 1
            time = i / 2
            if (time == startshoot + progProjectileTime):
                nodeFirewall -= progDamage * 3.5
            if nodeFirewall <= 0:
                return time + progInstallTime
##            if (time / nodeRegeneration == int(time / nodeRegeneration)):
##                p = nodeFirewall / 100
##                nodeFirewall += p
            if time / progHitInterval == int(time / progHitInterval):
                startshoot = time
                continue
        else:
            i += 1
            time= i / 2
            if (time == startshoot + progProjectileTime):
                nodeFirewall -= progDamage * 3.5
            if nodeFirewall <= 0:
                return time
            if (time / nodeRegeneration == int(time / nodeRegeneration)):
                p = nodeFirewall / 100
                nodeFirewall += p
            if time / progHitInterval == int(time / progHitInterval):
                startshoot = time
                continue
            
desc = ("Bot made by molchu and CodeWritten for a game called Hackers to make simple and complex calculations")

bot = commands.Bot(command_prefix = ".", description=desc)

with open('botToken.txt') as f:
    TOKEN = f.read()

@bot.event
async def on_ready():
    print("Up and running")

@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(color = 0xff0000)
    embed.add_field(name="Oops, an error occured!", value = error, inline = False)
    await ctx.send(embed=embed)

#the command below it a test command and adds no functions to the bot whatsoever
@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def calculate(ctx, *, args):
    argsList = args.split()
    with open("{}.json".format(argsList[0])) as f:
        temp1 = json.load(f)
        progDamage = temp1['DPS'][argsList[1]]
        progInstallTime = temp1["installTime"]
        progHitInterval = temp1["hitInterval"]
        progProjectileTime = temp1["projectileTime"]
    with open("{}.json".format(argsList[2])) as b:
        temp2 = json.load(b)
        nodeFirewall = temp2['fireWall'][argsList[3]]
        nodeRegeneration = temp2['firewallRegeneration']
    if progDamage * 3.5 < nodeFirewall / 100 * nodeRegeneration:
        await ctx.send("""The damage of the program is lower than the node's regeneration.
                       Assuming the node can't regenerate...""")
    takeOverTime = await timeCal(progDamage,progInstallTime,progHitInterval,progProjectileTime,nodeFirewall,nodeRegeneration)
    embed = discord.Embed(color=0x00ff00)
    minute = takeOverTime // 60
    second = takeOverTime - minute * 60
    embed.add_field(name='Calculation finished!', value= 'Node was taken in %s seconds (or %s minute(s) %s second(s))' %(takeOverTime,round(minute),round(second)),inline = False)
    await ctx.send(embed=embed)

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
            if argsList[1] == "compilationPrice" or argsList[1] == "DPS":
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
                await ctx.send(embed=embed)
            else:
                if len(argsList) == 2:
                    embed.add_field(name=argsList[0].capitalize() + ":", value=str(temp2), inline=True)
                    await ctx.send(embed=embed)
    except:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Oops, something went wrong!",value="Either there's something mistyped or missing, or this probably is a bug. Contact CodeWritten#4044 or molchu#2575 if you think this is a bug.", inline = False)
        await ctx.send(embed=embed)

@bot.command()
async def testDpsCalculate(ctx, *, args):
    argsList = args.split(" ")
    i = 0
    argsName = []
    argsLevel = []
    argsAmount = []
    while i <= argsList.len():
        argsName.append(argsList[i])
        i = i+3
    i = 1
    while i <= argsList.len():
        argsLevel.append(argsList[i])
        i = i+3
    i = 2
    while i <= argsList.len():
        argsAmount.append(argsList[i])
        i = i+3
    argsTuple = zip(argsName, argsLevel, argsAmount)
    dpsamount = 0.0
    boiii = 0.0
    for x, y, z in argsTuple:
        if x["isAStructure"] == False:
            boii = x["DPS"]
            dpsamount = dpsamount + boii[str(y)]*z
        else:
            boii = x["firewall"]
            boiii = boiii + (boii[str(y)] % dpsamount)
            dpsamount = 0
    embed=discord.Embed(color=0x00ff00)
    embed.add_field(name="Calculation Complete!",value="It took {} seconds to hack the base.".format(boiii))
    await ctx.send(embed=embed))

bot.run(TOKEN)
