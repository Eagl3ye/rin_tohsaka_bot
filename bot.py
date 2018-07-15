import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

import discord
from discord.ext import commands

rin = commands.Bot(command_prefix='r!')

@rin.event
async def on_ready():
    print('Logged in as...')
    print("Bot:",rin.user.name)
    print("User_ID:",rin.user.id)
    print('Changing presence...')
    await rin.change_presence(status=discord.Status.dnd, activity=discord.Game(name='with Daddy'))
    print("conn = ", conn)
@rin.command()
async def greet(msg):
    await msg.send(":smiley: :wave: Hello, there!")
@rin.command()
async def access(msg):
    cur = conn.cursor()
    cur.execute("SELECT * FROM test;")
    await msg.send(cur.fetchone())
    conn.commit()
    cur.close()
    conn.close()
    

BOT_TOKEN = os.environ['BOT_TOKEN']
rin.run(BOT_TOKEN)
