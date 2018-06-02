import bot
import config
import discord

client = discord.Client()
bot.registerCommands(client)

try:
    client.run(config.getValue("token"))
except discord.errors.LoginFailure:
    print("An improper token has been supplied in config.json")
    print("Exiting")
    raise SystemExit
