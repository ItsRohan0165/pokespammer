import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
import os  
 
bot = commands.Bot(command_prefix='!')

bot.remove_command('help')


 
@bot.event
async def on_ready():
    print("MI STO AVVIANDO... ASPETTA")
    print("SONO ONLINE! E PRONTO A SPAMMARE")
 
@bot.command(pass_context=True)
async def spam(ctx):
    await ctx.send("HERE WE GO!")
    time.sleep(0)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):

        channel = message.channel
        await channel.send("SPAWN")
        await channel.send("POKEMONS ")

 
bot.run (os.getenv("TOKEN"), bot=False)
