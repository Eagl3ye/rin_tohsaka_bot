import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

import discord
from discord.ext import commands

rin = commands.Bot(command_prefix='$')

@rin.event
async def on_ready():
    print('Logged in as...')
    print("Bot:",rin.user.name)
    print("User_ID:",rin.user.id)
    print('Changing presence...')
    await rin.change_presence(status=discord.Status.idle, activity=discord.Game(name='with Daddy'))
    print("conn = ", conn)
@rin.command()
async def greet(msg):
    await msg.send(":smiley: :wave: Hello, there!")
    
rin.run('NDAxNjE2NjkxNTkyNjkxNzEz.DTt_GQ.COQRZfPaW3wT8771iRP5EnxJmAM')
