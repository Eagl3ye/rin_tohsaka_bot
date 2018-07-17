#Imports
import os                                                       #OS lib
import discord                                                  #DISCORD API lib
from discord.ext import commands
bot = commands.Bot(command_prefix='r!')
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']                   
conn = psycopg2.connect(DATABASE_URL, sslmode='require')    
cur = conn.cursor()

def acgrant():
	await msg.send(":white_check_mark: ACCESS GRANTED :white_check_mark:")
	print("-=-=-ACCESS GRANTED-=-=-")
def acdeny():
	await msg.send(":no_entry: ACCESS DENIED :no_entry:")
	print("-x-x-ACCESS DENIED-x-x-")
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
	if(msg.author.id == 336068309789310979):
		acgrant()
		try:
			args = str(msg.message.content).split(" ")[1:]
			usr = str(args[0]), val = int(args[1])
			cur.execute("INSERT INTO kidz (usr_id, mono) VALUES (%s, %s);",(usr, val))
			print("\nINSERTED the VALUES INTO TABLE kidz...")
			print("UserID:",usr," | Value:",str(val),"\n")
			conn.commit()
		except psycopg2.IntegrityError:
			await msg.send(":lock: | Username already exists. Try again")
			pass
	else:
		acdeny()
		pass
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
	if(msg.author.id == 336068309789310979):
		acgrant()
		
		cur.execute("SELECT * FROM kidz;")
		dataset = (cur.fetchall())
		for data in dataset:
			respond = ("UserID: " + str(data[0]) +"\nValue: " + str(data[1])) 
			print(respond)
			await msg.send(respond)
		conn.commit()
	else:
		acdeny()
		pass
BOT_TOKEN = os.environ['BOT_TOKEN']
bot.run(BOT_TOKEN)
