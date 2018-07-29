#Imports
import os														#OS
import sys														#SYSTEM
import traceback												#TRACEBACK
import time														#TIME
import discord													#DISCORD API
from discord.ext import commands
bot = commands.Bot(command_prefix='r!')
import psycopg2													#DATABASE HANDLING
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[ EVENTS ]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@bot.event
async def on_command_error(msg, error):
	if isinstance(error, commands.CommandOnCooldown):
		await msg.send(":clock5: | **COOLDOWN: Retry again in {:.2f}s.**".format(error.retry_after))
		return

@bot.event
async def on_ready():
	print('Logged in as...')
	print("Bot:",bot.user.name)
	print("User_ID:",bot.user.id)
	print("Connection >> ", conn)
	print('Changing presence...')
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='Games'))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[ COGS ]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
extensions = ['Cogs.economy', 'Cogs.utility', 'Cogs.dev', 'Cogs.games']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

BOT_TOKEN = os.environ['BOT_TOKEN']
bot.run(BOT_TOKEN)
