#Imports
#import asyncio                                                 #ASYNCIO lib
#import time                                                    #TIME lib
import discord                                                  #DISCORD API lib
#from discord.ext.commands import Bot
from discord.ext import commands
rin = commands.Bot(command_prefix='r!')
import os                                                       
import psycopg2

@rin.event
async def on_ready():
    print('Logged in as...')
    print("Bot:",rin.user.name)
    print("User_ID:",rin.user.id)
    print('Changing presence...')
    await rin.change_presence(status=discord.Status.dnd, activity=discord.Game(name='with Daddy'))    
    
    #DATABASE HANDLING
    DATABASE_URL = os.environ['DATABASE_URL']                   
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')    
    cur = conn.cursor()
    print("conn = ", conn)
    
@rin.command()
async def wallet(msg):
    a = str(msg.message.content).split()
    await msg.send(a)
    #cur.execute("INSERT INTO test (usr_id, money) VALUES (,))
    
@rin.command()
async def myid(msg):
    await msg.send(msg.author.id)

@rin.command()
async def greet(msg):
    await msg.send(":smiley: :wave: Hello, there!")
    
@rin.command()
async def access(msg):
    
    cur.execute("SELECT * FROM test;")
    await msg.send(cur.fetchone())
    conn.commit()
    cur.close()
    
BOT_TOKEN = os.environ['BOT_TOKEN']
rin.run(BOT_TOKEN)
