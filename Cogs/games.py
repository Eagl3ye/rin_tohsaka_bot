import discord													#DISCORD API
from discord.ext import commands

class Games:
	def __init__(self, bot):
		self.bot = bot

	desc = "Werewolf takes place in a small village which is haunted by werewolves.\nEach player is secretly assigned a role - Werewolf, Villager, or Seer (a special Villager).\nThere is also a Moderator who controls the flow of the game.\nThe game alternates between night and day phases.\nAt night, the Werewolves secretly choose a Villager to kill.\nAlso, the Seer (if still alive) asks whether another player is a Werewolf or not.\nDuring the day, the Villager who was killed is revealed and is out of the game.\nThe remaining Villagers then vote on the player they suspect is a Werewolf.\nThat player reveals his/her role and is out of the game.\nWerewolves win when there are an equal number of Villagers and Werewolves.\nVillagers win when they have killed all Werewolves.\nWerewolf is a social game that requires no equipment to play, and can accommodate almost any large group of players."
	@commands.command(name=werewolf, description="{}".format(desc), aliases=['wolf','ww'], help="Plays Werewolf.", hidden=False, brief="Plays Werewolf.")
	# [+] WEREWOLF
	# [|] Plays Werewolf	
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def werewolf(self, options=None):
		if options == None:
			await msg.send(" ")

def setup(bot):
	bot.add_cog(Games(bot))