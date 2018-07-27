import discord													#DISCORD API
from discord.ext import commands

class Economy:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='daily')
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def daily(self, msg):
		user = "'%"+str(msg.author.id)+">%';"
		cur.execute("SELECT isDailyClaimed FROM kidz WHERE usr_id LIKE "+(user))
		claim_status = bool((cur.fetchall())[0][0])
		if claim_status:
			gmt = time.localtime()
			hrs, mins, secs = 23 - gmt[3], 59 - gmt[4], 59 - gmt[5]
			await msg.send(":gift: | **{}**, you still have to wait {}, {} and {} for your next daily reward.".format(msg.author.name,hrs,mins,secs))
		else:
			cur.execute("UPDATE kidz SET isDailyClaimed = true WHERE usr_id LIKE "+(user))
			cur.execute("SELECT mono FROM kidz WHERE usr_id LIKE "+(user))
			money = int((cur.fetchall())[0][0])
			cur.execute("UPDATE kidz SET mono = {} WHERE usr_id LIKE ".format(money + 50)+(user))
			await msg.send(":gift: | **{}**, you received :yen: 50 credits.".format(msg.author.name))
		conn.commit()
def setup(bot):
    bot.add_cog(Economy(bot))