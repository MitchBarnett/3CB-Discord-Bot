import bot
import config
import discord
import logging

file_handler = logging.FileHandler(filename='log.log')
stdout_handler = logging.StreamHandler()
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s',
    datefmt='%d-%b-%Y %I:%M:%S',
    handlers=handlers
)


client = discord.Client()
bot.registerCommands(client)

try:
    client.run(config.getValue("token"))
except discord.errors.LoginFailure:
    print("An improper token has been supplied in config.json")
    print("Exiting")
    raise SystemExit
