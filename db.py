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

@bot.event
async def on_command_error(msg, error):
	if isinstance(error, commands.CommandNotFound):
		return

async def run_reset():
	print("[SERVER] |\tReady...")
	while True:
		await asyncio.sleep(1)
		gmt = time.gmtime()
		hrs, mins, secs = (gmt[3] == 23), (gmt[4] == 59), (gmt[5] == 59)
		if hrs & mins & secs:
			cur.execute("UPDATE kidz SET isDailyClaimed = false;")
			conn.commit()
			print("[SERVER] |\tResetting dailies...")
			break

BOT_TOKEN = os.environ['BOT_TOKEN']
bot.run(BOT_TOKEN)









#cur.execute("SELECT * FROM kidz ORDER BY id ASC;")
#cur.execute("UPDATE kidz SET mono = 1 WHERE id = 1;")
#try:
#	cur.execute("CREATE TABLE kidz (id serial PRIMARY KEY, usr_id text UNIQUE, mono integer);")
#	print("\n\nCREATED TABLE NAMED kidz...\n\n")
#except psycopg2.DatabaseError:
#	conn.rollback()
#	pass
#cur.execute("ALTER TABLE kidz ADD daily bool")
#conn.commit()
#conn.close()