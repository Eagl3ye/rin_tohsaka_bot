import discord
from discord.ext import commands

rin = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(rin.user.name)
    print(rin.user.id)
    print('------')
    rin.change_presence(game=discord.Game(name='test'))

@bot.command()
async def greet(msg):
    await msg.send(":smiley: :wave: Hello, there!")
    
rin.run('NDAxNjE2NjkxNTkyNjkxNzEz.DTt_GQ.COQRZfPaW3wT8771iRP5EnxJmAM')
