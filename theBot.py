import json
import requests
import discord
from discord.ext import commands
import asyncio
import time
import subprocess
import os
import math

async def timeCal(progDamage,progInstallTime,progHitInterval,progProjectileTime,nodeFirewall,nodeRegeneration):
    time = 0
    i = 0
#the below variable is not being used
##    stunnedTime = 2
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
    presencelist = ["_----","-_---","--_--","---_-","----_"]
    while True:
        for i in range(0, len(presencelist)):
            game = discord.Game(presencelist[i])
            await asyncio.sleep(10)
            await bot.change_presence(status=discord.Status.online, activity = game)

@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(color = 0xff0000)
    embed.add_field(name="Oops, an error occured!", value = error, inline = False)
    await ctx.send(embed=embed)

@bot.command(description="Use dpsCalculate or projectileCalculate, as this command is OLD")
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

@bot.command(description="List the Parameter of a program or node. The syntax goes like this <programName> <category> <level (if required)>. For example: beamCannon DPS to list all dps values of beam cannon on all levels, or beamCannon DPS 21 to only list the level 21. Honestly you are better off using the wiki but this command exists so you might as well use it, if you break it then wiki is the answer.")
async def lsStat(ctx, *, args):
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

@bot.command(description="Unlike projectileCalculate, this command calculates raw DPS of all programs. Same syntax as projectileCalculate, so do help projectileCalculate to get the syntax. This does not account projectile travel and assumes every program has a hit interval of 1 second, and damage is also calculated for 1 second, so the number might be ever so off.")
async def dpsCalc(ctx, *, args):
    argsList = args.split(" ")
    i = 0
    argsName = []
    argsLevel = []
    argsAmount = []
    while i < len(argsList):
        argsName.append(argsList[i])
        i = i+3
    i = 1
    while i < len(argsList):
        argsLevel.append(argsList[i])
        i = i+3
    i = 2
    while i < len(argsList):
        argsAmount.append(argsList[i])
        i = i+3
    argsTuple = zip(argsName, argsLevel, argsAmount)
    dpsamount = 0.0
    boiii = 0.0
    for x, y, z in argsTuple:
        with open("{}.json".format(x), "r") as f:
            temp1 = json.load(f)
            if temp1["isAStructure"] == 0:
                boii = temp1["DPS"]
                dpsamount = dpsamount + float(boii[str(y)])*float(z)
                boiii = boiii + temp1["installTime"]
            else:
                boii = temp1["firewall"]
                boiii = boiii + (float(boii[str(y)]) / float(dpsamount))
                dpsamount = 0.0
    embed=discord.Embed(color=0x00ff00)
    embed.add_field(name="Calculation Complete!",value="It took {} seconds to hack the base.".format(boiii))
    await ctx.send(embed=embed)

@bot.command(description="This command calculates time based on projectile firing interval and install time of the program. The command assumes the projectile is instant hitting and does not take into account projectile time to reach the target. the syntax is as follows: command <programName> <level> <amountOfProgram> ... <nodeName> <level> <putARandomNumberHere>. The bot will stack all of the program damage prior to the node entering and then will calculate all of the collected dps against the node it finds, reset the dps and then start calculating again. So, you can port the whole base into text and the bot will calculate it.")
async def projCalc(ctx, *, args):
    argsList = args.split(" ")
    i = 0
    argsName = []
    argsLevel = []
    argsAmount = []
    while i < len(argsList):
        argsName.append(argsList[i])
        i = i+3
    i = 1
    while i < len(argsList):
        argsLevel.append(argsList[i])
        i = i+3
    i = 2
    while i < len(argsList):
        argsAmount.append(argsList[i])
        i = i+3
    argsTuple = zip(argsName, argsLevel, argsAmount)
    projamount = 0.0
    pleaseend = 0.0
    mysuffering = 0.0
    weDontHaveTime = 0.0
    temporaryvalue = 0
    for x, y, z in argsTuple:
        with open("{}.json".format(x), "r") as f:
            temp1 = json.load(f)
            if temp1["isAStructure"] == 0:
                temp2 = temp1["DPS"]
                temp3 = temp1["installTime"]
                temp4 = temp1["hitInterval"]
                if mysuffering < temp4:
                    mysuffering = temp4
                if pleaseend < temp3:
                    pleaseend = temp3
                projamount = projamount + float(temp2[str(y)])*float(z)
                temporaryvalue = 0
            else:
                temp2 = temp1["firewall"]
                structureFirewall = temp2[str(y)]
                floatedStructureFirewall = float(structureFirewall)
                while floatedStructureFirewall > 0.0:
                    if projamount <= 0:
                        break
                    if temporaryvalue == 1:
                        weDontHaveTime = weDontHaveTime + mysuffering
                        floatedStructureFirewall = floatedStructureFirewall - projamount
                    temporaryvalue = 1
                weDontHaveTime = weDontHaveTime + pleaseend
    embed=discord.Embed(color=0x00ff00)
    embed.add_field(name="Calculation Complete!",value="It took {} seconds to hack the base.".format(weDontHaveTime))
    await ctx.send(embed=embed)
bot.run(TOKEN)
