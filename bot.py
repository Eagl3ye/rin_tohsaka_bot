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
	print("conn = ", conn)
	print('Changing presence...')
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='with Daddy'))

@bot.command()
async def create(msg):
	if(msg.author.id == 336068309789310979):
		await msg.send(":white_check_mark: ACCESS GRANTED :white_check_mark:")
		print("-=-=-ACCESS GRANTED-=-=-")
		try:
			args = str(msg.message.content).split(" ")[1:]
			usr, val = str(args[0]), int(args[1])
			cur.execute("INSERT INTO kidz (usr_id, mono) VALUES (%s, %s);",(usr, val))
			print("\nINSERTED the VALUES INTO TABLE kidz...")
			print("UserID:",usr," | Value:",str(val),"\n")
			conn.commit()
		except psycopg2.IntegrityError:
			await msg.send(":lock: | Username already exists. Try again")
			conn.rollback()
			pass
	else:
		await msg.send(":no_entry: ACCESS DENIED :no_entry:")
		print("-x-x-ACCESS DENIED-x-x-")
		pass
@bot.command()
async def wallet(msg):
	args = str(msg.message.content).split()
	auth = "'%"+str(msg.author.id)+">%';"
	ctxlen = len(args)
	if ctxlen > 1:
<<<<<<< HEAD
		auth = "'%"+str(args[1])[2:-1]+"%';"
		print(str(args[1])[2:-1])
		#cur.execute("SELECT mono FROM kidz WHERE usr_id LIKE "+(auth))
		#money = int((cur.fetchall())[0][0])
		#if money == 0:
		#	await msg.send(":credit_card: | **He/She has no credits in his/her wallet**")
		#elif money == 1:
		#	await msg.send(":credit_card: | **He/She has {:s} credit in his/her wallet**".format(str(money)))
		#else:
		#	await msg.send(":credit_card: | **He/She has {:s} credits in his/her wallet**".format(str(money)))
		#conn.commit()
		pass
=======
		auth = "'%"+str(args[1])+">%';"
	cur.execute("SELECT mono FROM kidz WHERE usr_id LIKE "+(auth))
	money = int((cur.fetchall())[0][0])
	print("MONEY: ",money)
	if money == 0:
		await msg.send(":credit_card: | **You have no money in your wallet**")
	elif money == 1:
		await msg.send(":credit_card: | **You have {:s} credit in your wallet**".format(str(money)))
>>>>>>> parent of 8de477e... major fix
	else:
		await msg.send(":credit_card: | **You have {:s} credits in your wallet**".format(str(money)))
	conn.commit()
	
@bot.command()
async def myid(msg):
	await msg.send(msg.author.id)
	await msg.send(str(msg.author.id))
@bot.command()
async def greet(msg):
	await msg.send(":smiley: :wave: Hello, there!")
	
@bot.command()
async def access(msg):
	if(msg.author.id == 336068309789310979):
		await msg.send(":white_check_mark: ACCESS GRANTED :white_check_mark:")
		print("-=-=-ACCESS GRANTED-=-=-")

		try:
			cur.execute("SELECT * FROM kidz;")
			dataset = (cur.fetchall())
			embed = discord.Embed(title="|| BANK ACCOUNTS", color=0xff2020)
			for tag, data in enumerate(dataset):
				embed.add_field(name="[ "+(str(tag+1))+" ] - UserID: "+str(data[1])+"", value="Money: "+str(data[2]), inline=False)
			await msg.send(embed=embed)
			conn.commit()
		except psycopg2.InternalError:
			#conn.rollback()
			pass
	else:
		await msg.send(":no_entry: ACCESS DENIED :no_entry:")
		print("-x-x-ACCESS DENIED-x-x-")
		pass
BOT_TOKEN = os.environ['BOT_TOKEN']
bot.run(BOT_TOKEN)
