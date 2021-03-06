import os														#OS
import time														#TIME
import discord													#DISCORD API
from discord.ext import commands
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
conn.close()

class Utility:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='greet', aliases=['Hello'], help="Greets the User.", hidden=False, brief="Greets the User.")
	# [+] GREET
	# [|] Greets the User
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def greet(self, msg):
		await msg.send(":smiley: :wave: Hello, there!")

	@commands.command(name='now', aliases=['time','timenow'], help="Displays the current server time.", hidden=False, brief="Displays the current server time.")	
	# [+] NOW
	# [|] Displays the current server time
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def now(self, msg):
		clt = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime())
		await msg.send("```python\n['SERVER TIME']\n\nAsia/Manila UTC +08:00\n#>\t{}```".format(clt))

	@commands.command(name='myid', aliases=['id'], help="Shows the User's unique Discord ID.", hidden=False, brief="Shows the User's unique Discord ID.")
	# [+] MYID
	# [|] Shows the User's unique Discord ID
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def myid(self, msg):
		await msg.send(msg.author.id)
		print((str(args[1]))[3:-1])

def setup(bot):
    bot.add_cog(Utility(bot))