import discord
import asyncio
import config
import serverinfo

def registerCommands(client):
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
            await client.send_message(message.channel, "test")
