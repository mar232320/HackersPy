import discord
import random
from discord.ext import commands

class funs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="We dont know what this does, maybe its an easter egg?", hidden = True)
    async def suffer(self, ctx):
        embed = discord.Embed(color = 0xff0000)
        embed.add_field(name="The Bang Bang created everything. however there was never nothing, and thats why there is always nothing. nothing is everywhere, its so every you dont need a where", value = str, inline = False)
        await ctx.send(embed=embed)

    @commands.command(description = "Lists nodeNames and keys aswell as programNames and keys", aliases = ['wtf'])
    async def listitems(self, ctx):
        await ctx.send ("Programs: beamCannon (doesnt work with projCalc as beam is not a projectile) shuriken blaster maniac worm\n Nodes: codeGate (does not have filter emulation as of now) core serverFarm database coinMiner coinMixer scanner sentry turret blackIce guardian evolver,\n Keys: DPS (progs) firewall (Nodes)")

    @commands.command(hidden = True)
    async def killAmethysm(self, ctx):
        randkill = ["Gun", "Drowning", "Molchu"]
        chosenrandkill = random.choice(randkill)
        if chosenrandkill == "Gun":
            await ctx.send("Amethysm was shot by a gun! Bang! he's dead!")
        elif chosenrandkill == "Drowning":
            await ctx.send("Molchu threw Amethysm off a glacier and he couldn't swim, :(")
        elif chosenrandkill == "Molchu":
            await ctx.send("Molchu and Amethysm Dueled with swords, molchu stabs Amethysm and he dies :(")

    @commands.command(hidden = True)
    async def killCode(self, ctx):
        randkill = ["Gun", "Drowning", "Molchu"]
        chosenrandkill = random.choice(randkill)
        if chosenrandkill == "Gun":
            await ctx.send("CodeWritten was shot by a gun! Bang! he's dead!")
        elif chosenrandkill == "Drowning":
            await ctx.send("Molchu threw CodeWritten off a glacier and he couldn't swim, :(")
        elif chosenrandkill == "Molchu":
            await ctx.send("Molchu and CodeWritten Dueled with swords, molchu stabs CodeWritten and he dies :(")

    @commands.command(hidden = True)
    async def killMolchu(self, ctx):
        randkill = ["Gun", "Drowning", "Molchu"]
        chosenrandkill = random.choice(randkill)
        if chosenrandkill == "Gun":
            await ctx.send("Molchu was shot by a gun! Bang! he's dead!")
        elif chosenrandkill == "Drowning":
            await ctx.send("CodeWritten threw Molchu off a glacier and he couldn't swim, :(")
        elif chosenrandkill == "Molchu":
            await ctx.send("Molchu and CodeWritten Dueled with swords, CodeWritten stabs molchu and he dies :(")

    @commands.command(brief = '`Alexa kill {member}`', description="Kill someone you hate. More death messages coming soon!")
    async def kill(self,ctx,member:discord.Member=None):
        if member is None:
            await ctx.send("You decided to look around for someone to kill with your new gun, but there wasn't anyone nearby. You ended up killing yourself.")
        else:
            a = random.randint(1,10)
            if a == 1:
                await ctx.send(member.name + " was filled with " + ctx.author.name + "'s worms.")
            elif a == 2:
                await ctx.send(member.name + " was brutally killed after stating that beam cannon is better than shuriken.")
            elif a == 3:
                await ctx.send(member.name + " was dead trying to triple protector a node. They forgot they didn't have any protectors left.")
            elif a == 4:
                await ctx.send(member.name + " was captured by a hit of maniac in the face by " + ctx.author.name + ".")
            elif a == 5:
                await ctx.send(ctx.author.name + " successfully tricapped " + member.name + "'s base with only a level 1 worm.")
            elif a == 6:
                await ctx.send(member.name + " along with 3 other nodes were wraithed by " + ctx.author.name + ". That damn scanner didn't do it's job!")
            elif a == 7:
                await ctx.send(member.name + " was brutally killed in real life while doing SC Sector 13 mission.")
            elif a == 8:
                await ctx.send(member.name + " commited attacking " + ctx.author.name + "'s base without a protector.")
            elif a == 9:
                await ctx.send(member.name + "'s network cable was unplugged by their 3 years old brother while attacking " + ctx.author.name + ".")
            elif a == 10:
                await ctx.send(member.name + " was brutally triple-blastered by " + ctx.author.name + ".")

def setup(bot):
    bot.add_cog(funs(bot))

