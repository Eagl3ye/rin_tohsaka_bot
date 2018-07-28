import os														#OS
import time														#TIME
import asyncio													#ASYNCIO
import discord													#DISCORD API
from discord.ext import commands
bot = commands.Bot(command_prefix='r!')
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
DEV = os.environ['DEV']

class Dev:
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(hidden=True)
	async def access(self, msg):
		if(msg.author.id == int(DEV)):
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

	@commands.command(hidden=True)
	async def create(self, msg):
		if(msg.author.id == int(DEV)):
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

	@commands.command(hidden=True)
	async def test(self, msg):
		if(msg.author.id == int(DEV)):
			await msg.send(":white_check_mark: ACCESS GRANTED :white_check_mark:")
			print("-=-=-ACCESS GRANTED-=-=-")
			TZ = os.environ['TZ']
			time.tzset()
			await msg.send(time.localtime())
			cur.execute("SELECT * FROM kidz;")
			await msg.send((cur.fetchall()))	
		else:
			await msg.send(":no_entry: ACCESS DENIED :no_entry:")
			print("-x-x-ACCESS DENIED-x-x-")
			pass

def setup(bot):
	bot.add_cog(Dev(bot))