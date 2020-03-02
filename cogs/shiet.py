import discord
import random
from discord.ext import commands
import asyncio
CodeWLogin= 0
AmethysmLogin= 0
THKLogin= 0
CodeWPassword= "awaitYourMum"
AmethysmPassword= "None"
THKPassword= "None"
class stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = True)
    async def pleaseendme(self, ctx):
        channel = bot.get_channel()
        await ctx.author.send("Please end me")
        await channel.send("Please end me") 


    @commands.command(hidden = True)
    async def login(self, ctx, args1):
        execuser = ctx.author.id
        if execuser in (436646726204653589, 525334420467744768, 419742289188093952):
            if execuser == 419742289188093952 and args1 == THKPassword:
                THKLogin = 1
                await ctx.send("Welcome, THK")

            elif execuser == 525334420467744768 and args1 == AmethysmPassword:
                AmethysmLogin = 1
                await ctx.send("Welcome, Amethysm")

            elif execuser == 436646726204653589 and args1 == CodeWPassword:
                CodeWLogin = 1
                await ctx.send("Welcome, [God]CodeWritten")

def setup(bot):
    bot.add_cog(stuff(bot))