import os														#OS
import time														#TIME
import discord													#DISCORD API
from discord.ext import commands
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

class Utility:
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name='now', aliases=['time','timenow'])	
	# [+] NOW
	# [|] Displays the current server time
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def now(self, msg):
		clt = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime())
		await msg.send("```python\n['SERVER TIME']\n\nAsia/Manila UTC +08:00\n#>\t{}```".format(clt))

	@commands.command(name='myid', aliases=['id'])
	# [+] MYID
	# [|] Shows the unique Discord ID
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def myid(self, msg):
		args = str(msg.message.content).split()
		await msg.send(msg.author.id)
		print((str(args[1]))[3:-1])

def setup(bot):
    bot.add_cog(Utility(bot))