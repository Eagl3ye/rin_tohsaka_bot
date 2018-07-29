import os														#OS
import discord													#DISCORD API
from discord.ext import commands
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
is_game_running = False

class Games:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="werewolf", description="Type `r![werewolf|wolf|ww] [info]` for an in-depth description.", aliases=['wolf','ww'], help="Plays Werewolf.", hidden=False, brief="Plays Werewolf.")
	# [+] WEREWOLF
	# [|] Plays Werewolf	
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def werewolf(self, msg, options=None):
		if options == None:
			#Display help
			pass
		elif options == "create":
			if is_game_running:
				await msg.send(":gear: | `An instance of the game is already running...`")
			else:
				try:
					cur.execute("CREATE TABLE werewolf (id serial PRIMARY KEY, usr_id text UNIQUE, name text, is_dead boolean, role text);")
					conn.commit()
					await msg.send(":white_check_mark: | **WEREWOLF**: LOBBY CREATED!\n\nType `r![werewolf|wolf|ww] [join]` to join")
					is_game_running = True
				except psycopg2.DatabaseError:
					conn.rollback()
					await msg.send(":gear: | `An instance of the game is already running...`")
		elif options == "join":
			if is_game_running:
				authid = msg.author.id
				authname = msg.author.name
				try:
					cur.execute("INSERT INTO werewolf (usr_id, name, is_dead) VALUES ({}, {}, False);".format(authid, authname))
					cur.execute("SELECT * FROM werewolf;")
					joined_count = int(max(cur.fetchall())[0]) + 1
					embed=discord.Embed(color=0x5050a0)
					embed.add_field(name="Game: Werewolf", value="[ "+joined_count+" / 4 Players joined the game ]", inline=False)
					embed.set_footer(text="r!werewolf join - to join the game")
					await msg.send(embed=embed)
					conn.commit()
				except psycopg2.IntegrityError:
					await msg.send(":lock: | **{}**, You already joined the game.".format(authname))
					conn.rollback()
					pass
			else:
				await msg.send(":negative_squared_cross_mark: | **WEREWOLF**: NO LOBBY FOUND!\n\nType `r![werewolf|wolf|ww] [create]` to create a lobby")
		elif options == "info":
			await msg.send("```\nWerewolf takes place in a small village which is haunted by werewolves.\n\nEach player is secretly assigned a role - Werewolf, Villager, or Seer (a special Villager).\nThere is also a Moderator who controls the flow of the game.\nThe game alternates between night and day phases.\nAt night, the Werewolves secretly choose a Villager to kill.\nAlso, the Seer (if still alive) asks whether another player is a Werewolf or not.\nDuring the day, the Villager who was killed is revealed and is out of the game.\n\nThe remaining Villagers then vote on the player they suspect is a Werewolf.\nThat player reveals his/her role and is out of the game.\nWerewolves win when there are an equal number of Villagers and Werewolves.\nVillagers win when they have killed all Werewolves.\n```")
		elif options == "leave":
			if is_game_running:
				cur.execute("DROP TABLE werewolf;")
				is_game_running = False
				conn.commit()
				await msg.send(":gear: | `An instance of the game has been removed.`")
			else:
				await msg.send(":negative_squared_cross_mark: | **WEREWOLF**: NO LOBBY FOUND!\n\nType `r![werewolf|wolf|ww] [create]` to create a lobby")
		else:
			pass

def setup(bot):
	bot.add_cog(Games(bot))