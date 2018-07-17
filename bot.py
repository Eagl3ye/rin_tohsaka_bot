#Imports
import os                                                       #OS lib
import discord                                                  #DISCORD API lib
from discord.ext import commands
bot = commands.Bot(command_prefix='r!')
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']                   
conn = psycopg2.connect(DATABASE_URL, sslmode='require')    
cur = conn.cursor()
	
@bot.event
async def on_ready():
	print('Logged in as...')
	print("Bot:",bot.user.name)
	print("User_ID:",bot.user.id)
	print('Changing presence...')
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='with Daddy'))    
	print("conn = ", conn)

@bot.command()
async def create(msg):
	args = str(msg.message.content).split(" ")[1:]
	usr = str(args[0])
	val = int(args[1])
	#cur.execute("INSERT INTO kidz (usr_id, mono) VALUES ({:s}, {:s});".format(usr,val))
	cur.execute("INSERT INTO kidz (usr_id, mono) VALUES (%s, %s);",(usr, val))
	print("INSERTED the VALUES INTO TABLE kidz...")
	print("UserID:",usr," | Value:",str(val))
	conn.commit()
	
@bot.command()
async def wallet(msg):
	args = str(msg.message.content).split()[1:]
	#if count(args) > 1:
		#code
	#else:
		#show wallet
	await msg.send(args[1:])
	#cur.execute("INSERT INTO test (usr_id, money) VALUES (,))
	
@bot.command()
async def myid(msg):
	await msg.send(msg.author.id)

@bot.command()
async def greet(msg):
	await msg.send(":smiley: :wave: Hello, there!")
	
@bot.command()
async def access(msg):
	cur.execute("SELECT usr_id FROM kidz;")
	a = (cur.fetchall())
	print("UserID:",a)
	await msg.send(a)
	conn.commit()
	
BOT_TOKEN = os.environ['BOT_TOKEN']
bot.run(BOT_TOKEN)
