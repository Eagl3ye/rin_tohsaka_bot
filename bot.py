#Imports
#import asyncio                                                 #ASYNCIO lib
#import time                                                    #TIME lib
import os                                                       #OS lib

#DISCORD API lib
import discord                                                  
#from discord.ext.commands import Bot
from discord.ext import commands
rin = commands.Bot(command_prefix='r!')

#DATABASE HANDLING                                                      
import psycopg2
DATABASE_URL = os.environ['DATABASE_URL']                   
conn = psycopg2.connect(DATABASE_URL, sslmode='require')    
cur = conn.cursor()
	
@rin.event
async def on_ready():
	print('Logged in as...')
	print("Bot:",rin.user.name)
	print("User_ID:",rin.user.id)
	print('Changing presence...')
	await rin.change_presence(status=discord.Status.dnd, activity=discord.Game(name='with Daddy'))    
	print("conn = ", conn)

@rin.command()
async def create(msg):
	args = str(msg.message.content).split(" ")[1:]
	usr = str(args[0])
	val = int(args[1])
	#cur.execute("INSERT INTO kidz (usr_id, mono) VALUES ({:s}, {:s});".format(usr,val))
	cur.execute("INSERT INTO kidz (usr_id, mono) VALUES (%s, %s);",(usr, val))
	print("INSERTED the VALUES INTO TABLE kidz...")
	conn.commit()
	
@rin.command()
async def wallet(msg):
	args = str(msg.message.content).split()[1:]
	#if count(args) > 1:
		#code
	#else:
		#show wallet
	await msg.send(args[1:])
	#cur.execute("INSERT INTO test (usr_id, money) VALUES (,))
	
@rin.command()
async def myid(msg):
	await msg.send(msg.author.id)

@rin.command()
async def greet(msg):
	await msg.send(":smiley: :wave: Hello, there!")
	
@rin.command()
async def access(msg):
	cur.execute("SELECT * FROM kidz;")
	a = (cur.fetchone())[0]
	await msg.send(a)
	conn.commit()
	
BOT_TOKEN = os.environ['BOT_TOKEN']
rin.run(BOT_TOKEN)
