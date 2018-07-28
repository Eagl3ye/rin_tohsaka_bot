import os														#OS
import time														#TIME
import discord													#DISCORD API
from discord.ext import commands
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

class Economy:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='daily', help="Claims the daily reward.", hidden=False, brief="Claims the daily reward.")
	# [+] DAILY
	# [|] Claim the daily reward
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def daily(self, msg):
		user = "'%"+str(msg.author.id)+">%';"
		cur.execute("SELECT isDailyClaimed FROM kidz WHERE usr_id LIKE "+(user))
		claim_status = bool((cur.fetchall())[0][0])
		if claim_status:
			gmt = time.localtime()
			hrs, mins, secs = 23 - gmt[3], 59 - gmt[4], 59 - gmt[5]
			await msg.send(":gift: | **{}**, you still have to wait {} hour/s, {} minute/s and {} second/s for your next daily reward.".format(msg.author.name,hrs,mins,secs))
		else:
			cur.execute("UPDATE kidz SET isDailyClaimed = true WHERE usr_id LIKE "+(user))
			cur.execute("SELECT mono FROM kidz WHERE usr_id LIKE "+(user))
			money = int((cur.fetchall())[0][0])
			cur.execute("UPDATE kidz SET mono = {} WHERE usr_id LIKE ".format(money + 50)+(user))
			await msg.send(":gift: | **{}**, you received :yen: 50 credits.".format(msg.author.name))
		conn.commit()

	@commands.command(name='wallet', help="Displays the User's or Target User's credits in the wallet.", hidden=False, brief="Displays the User's or Target User's credits in the wallet.")
	# [+] WALLET
	# [|] Displays the User's or Target User's credits in the wallet
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def wallet(self, msg, user:str=None):
		money = 0;
		if user is None:
			newuser = "'%"+str(msg.author.id)+">%';"
			cur.execute("SELECT mono FROM kidz WHERE usr_id LIKE "+(newuser))
			money = int((cur.fetchall())[0][0])
		else:
			user = "'%"+(user)[3:-1]+"%';"
			cur.execute("SELECT mono FROM kidz WHERE usr_id LIKE "+(user))
			money = int((cur.fetchall())[0][0])

		if money == 0:
			await msg.send(":credit_card: | **Wallet is empty**")
		elif money == 1:
			await msg.send(":credit_card: | **{:s} credit**".format(str(money)))
		else:
			await msg.send(":credit_card: | **{:s} credits**".format(str(money)))
		conn.commit()

def setup(bot):
	bot.add_cog(Economy(bot))