import discord
import random
from discord.ext import commands
CodeWLogin= 0
AmethysmLogin= 0
THKLogin= 0
CodeWPassword= "awaitYourMum"
AmethysmPassword= "None"
THKPassword= "None"
class stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(hidden = True)
    async def pleaseendme(ctx):
        channel = bot.get_channel()
        await ctx.author.send("Please end me")
        await ctx.channel.send("Please end me") 


    @bot.command(hidden = True)
    async def login(ctx, args1):
        execuser = ctx.author.id
        if execuser in (436646726204653589, 525334420467744768, 419742289188093952):
            if execuser == 419742289188093952 and arg1 == THKPassword:
                THKLogin = 1
                await ctx.send("Welcome, THK")

            elif execuser == 525334420467744768 and args1 == AmethysmPassword:
                AmethysmLogin = 1
                await ctx.send("Welcome, Amethysm")

            elif execuser == 436646726204653589 and args1 == CodeWPassword:
                CodeWLogin = 1
                await ctx.send("Welcome, [God]CodeWritten")