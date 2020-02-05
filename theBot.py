#Module Importation
import json
import requests
import discord
from discord.ext import commands
import asyncio
import time
import subprocess
import os
import math
import sys

#Bot Functionality
async def timeCal(progDamage,progInstallTime,progHitInterval,progProjectileTime,nodeFirewall,nodeRegeneration):
    time = 0
    i = 0
#the below variable is not being used
##    stunnedTime = 2
#Pre-Calculation Definition & Math Layout
    startshoot = -10000
    while True:
        if progDamage * 3.5 < nodeFirewall / 100 * nodeRegeneration:   
            i += 1
            time = i / 2
            if (time == startshoot + progProjectileTime):
                nodeFirewall -= progDamage * 3.5
            if nodeFirewall <= 0:
                return time + progInstallTime
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
            
#Commands Def
desc = ("Bot made by molchu, CodeWritten and Amethysm for a game called Hackers to make simple and complex calculations")

bot = commands.Bot(command_prefix = ".", description=desc, help_command = None)
bot.remove_command('help')


with open('botToken.txt') as f:
    TOKEN = f.read()

@bot.event
async def on_ready():
    print("Up and running")
    presencelist = ["Working on Taking Over The World","Competing with Keyboard Cat","Playing Dead","Listening to 2 Servers","Idling but not Idling"]
    while True:
        for i in range(0, len(presencelist)):
            game = discord.Game(presencelist[i])
            await bot.change_presence(status=discord.Status.online, activity = game)
            await asyncio.sleep(120)
##
@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(color = 0xff0000)
    embed.add_field(name="Oops, an error occured!", value = error, inline = False)
    await ctx.send(embed=embed)
    print(error)

@bot.command(aliases = ['o','k','b','oo','m','e','r'], description= 'no shiet', brief = "does nothing")
async def test(ctx):
    await ctx.send('ok boomer')

@bot.command(description="Shows this help page.", brief="`.help [command]`")
async def help(ctx, *, args=None):
    if args is not None:
        b = args.split()
    try:
        if args is None:
            embed = discord.Embed(color=0x00ff00, title = desc)
            a = list(bot.commands)
            for i in range(0,len(bot.commands)):
                if a[i].hidden == True:
                    pass
                else:
                    embed.add_field(name=a[i].name, value = str(a[i].description),inline=False)
            embed.set_footer(text="For more information on any command type |.help <command>| (work in progress)")
            await ctx.author.send(embed=embed)
            await ctx.send('A message with the help page sent to your DM!')
        elif len(b) == 1:
            reqCommand = bot.get_command(b[0])
            embed = discord.Embed(color=0x00ff00,title = "Help page for " + reqCommand.name + " command:")
            embed.add_field(name="Usage: ", value = str(reqCommand.brief),inline=True)
            if len(reqCommand.aliases) != 0:
                embed.add_field(name="Aliases: ", value = str(reqCommand.aliases), inline = False)
            else:
                embed.add_field(name="Aliases: ", value = "No aliases", inline = False)
            embed.add_field(name="Description on usage:", value = reqCommand.description,inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("Failed sending the message with the help page. Did you block the bot?")

@bot.command(description = "Return the latency of the bot. Can also be triggered with .ping", aliases=['ping'], brief = "`.ping`")
async def latency(ctx):
    await ctx.send("Pong! "  + str(round(bot.latency * 100)) + "ms.")
    
@bot.command(description="Use dpsCalculate or projectileCalculate, as this command is outdated",brief='Dead command here')
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

@bot.command(description="We dont know what this does, maybe its an easter egg?", hidden = True)
async def suffer(ctx):
    embed = discord.Embed(color = 0xff0000)
    embed.add_field(name="The Bang Bang created everything. however there was never nothing, and thats why there is always nothing. nothing is everywhere, its so every you dont need a where", value = str, inline = False)
    await ctx.send(embed=embed)

@bot.command(brief = "`lsStat {program/node} {stat} [level] `", aliases=['info'],description="List the Parameter of a program or node. The syntax goes like this <programName> <category> <level (if required)>. For example: beamCannon DPS to list all dps values of beam cannon on all levels, or beamCannon DPS 21 to only list the level 21. Honestly you are better off using the wiki but this command exists so you might as well use it, if you break it then wiki is the answer.")
async def lsStat(ctx, *, args):
    argsList = args.split(' ')
    embed=discord.Embed(color=0x00ff00)
    with open("{}.json".format(argsList[0]), "r") as f:
        temp1 = json.load(f)
    if len(argsList) == 3:
        if 'imageAddress' in temp1.keys():
            embed.set_thumbnail(url = temp1['imageAddress'][argsList[2]])
        embed.add_field(name= "Level " + argsList[2] + " " + argsList[0].capitalize() + "'s "  + argsList[1] + ":", value = temp1[argsList[1]][argsList[2]],inline=True)
        await ctx.send(embed=embed)
    elif len(argsList) == 2 and isinstance(temp1[argsList[1]], dict):
        if 'imageAddress' in temp1.keys() and isinstance(temp1['imageAddress'], dict) is False:
            embed.set_thumbnail(url = temp1['imageAddress'])
        for i in range(0,len(temp1[argsList[1]])):
            a = []
            b = []
            for key in temp1[argsList[1]].keys():
                a.append(key)
            for value in temp1[argsList[1]].values():
                b.append(value)
            name = a[i]
            value = b[i]
            embed.add_field(name='Level ' + str(name), value = value, inline=True   )
        await ctx.send(embed=embed)
    elif len(argsList) == 2 and isinstance(temp1[argsList[1]],dict) is False:
        value = temp1[argsList[1]]
        embed.add_field(name = argsList[0].capitalize() + " " + argsList[0].capitalize() + "'s " + argsList[1].capitalize(), value = value, inline = False)
        await ctx.send(embed=embed)
        
@bot.command(brief = "`.dpsCalc {program} {level} {amount} {node} {level} 0 (repeat if needed)`", description="Unlike projectileCalculate, this command calculates raw DPS of all programs. Same syntax as projectileCalculate, so do help projectileCalculate to get the syntax. This does not account projectile travel and assumes every program has a hit interval of 1 second, and damage is also calculated for 1 second, so the number might be ever so off.")
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

@bot.command(description="Restarts The Bot's source file, use if bot freezes etc, [OWNER]")
async def shutdown(ctx):
     if ctx.author.id == "436646726204653589" or "525334420467744768" or "218142353674731520":
        embed = discord.Embed(color = 0xff0000)
        embed.add_field(name="Shutdown Command Sent, Bot Rebooting in 3 seconds", value = str, inline = False)
        await ctx.send(embed=embed)
        await asyncio.sleep(3)
        os.execl(sys.executable, sys.executable, * sys.argv)
        await bot.close()
        os.system("py -3 theBot.py")

bot.run(TOKEN)
