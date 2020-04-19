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
    print("ready")
    print("online")

colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}

list = [
    "May you be gifted with life’s biggest joys and never-ending bliss. After all, you yourself are a gift to earth. Happy Birthday to you!",
    "Wishing you a wonderful day and all the most amazing things on your Big Day!, Happy Birthday",
    "All things are sweet and bright. May you have a lovely birthday Night. Happy Birthday!!",
    "Be happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! Happy Birthday!!",
    "A friend like you is more priceless than the most beautiful diamond. You are not only strong and wise, but kind and thoughtful as well. Your birthday is the perfect opportunity to show you how much we care and how grateful we are to have you . Happy birthday!",
    "Soon you’re going to start a new year of your life and I hope this coming year will bring every success you deserve.Hope your birthday is as wonderful and extraordinary as you are"
]

@bot.command(pass_context=True)
async def wish(ctx,):
    await ctx.send("HERE WE GO!")
    time.sleep(0)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
       
        color_list = [c for c in colors.values()]
        hop=random.choice(list)
        e = discord.Embed(title="Happy Birthday Bushido! :partying_face::partying_face:", description=f"{hop}", color=random.choice(color_list))
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/699538048945225778/701411667313033226/black-calligraphy-happy-birthday-fireworks-wishes-animated-gif.gif")
        await ctx.send(embed=e)
        time.sleep(5)
        

 
bot.run(os.getenv('token'))

