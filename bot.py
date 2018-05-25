import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    client.servers
    print("Running discord.py version: " + discord.__version__)
    print('------')
    print('Logged in as: ' + str(client.user))
    print('------')
    print("Running on:")
    for server in client.servers:
        print("%s as %s " % (server.name, server.me.display_name))
    print('------')
    
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        client.send_message("test")        
client.run('TOKEN')
