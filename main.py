import bot
import config
import discord
import logging

client = discord.Client()
bot.registerCommands(client)

FORMAT = '%(asctime)s %(message)s'
DATE = '%d-%b-%Y %I:%M:%S'
logging.basicConfig(filename="log.log",level=logging.INFO,format=FORMAT,datefmt=DATE)
logger = logging.getLogger('Stackoverflow log')
logger.info('Info 1')

try:
    client.run(config.getValue("token"))
except discord.errors.LoginFailure:
    print("An improper token has been supplied in config.json")
    print("Exiting")
    raise SystemExit
