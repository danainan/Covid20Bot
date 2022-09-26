
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='+',help_command=None) 
@bot.event
async def on_ready() :
    print(f"logged in as{bot.user}") 

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Covid20Bot HELP!!!", description="All Available Bot Commands" ,Color=0x8646c2)
    emBed.add_field(name='help', value='ช่วยตัวเองเหอะไอเหี้ย', inline=False)
    emBed.add_field(name='user', value='ไม่ต้องรู้หรอก', inline=False)
    emBed.add_field(name='play', value='เล่นเพลงเหี้ยไรหล่ะ?', inline=False)
    await ctx.channel.send(embed=emBed)

@bot.event
async def on_message(message) : 
    if message.content.startswith('+covid20') :
       await message.channel.send('ว่าไง ไอสัส!!! กูคือ '+str(bot.user.name)+' มีไรป่าว') 
    elif message.content.startswith('+ไอบอท') : 
       await message.channel.send('มึงจะทำไม')
    elif message.content.startswith('+user'):
        await message.channel.send('ไอเหี้ย '+str(message.author.name)+' เป็น Covid20')
    elif message.content.startswith('555' or '555+'or '55' or '5555'):
        await message.channel.send('ตลกหรอไอสัส!!!')


bot.run('Token') 
