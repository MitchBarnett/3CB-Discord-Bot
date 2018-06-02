import discord
import asyncio
import config
import serverInfo

def registerCommands(client):
    @client.event
    async def on_ready():
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
        if message.content.startswith("!mission"):
            info = serverInfo.getInfo()
            await client.send_message(message.channel, "The current mission is %s on %s" % (info.game, info.map))

        elif message.content.startswith("!players"):
            info = serverInfo.getInfo()
            await client.send_message(message.channel, "There is currently %i players online" % info.player_count)

        elif message.content.startswith("!who"):
            players = serverInfo.getPlayers()
            embed = discord.Embed(title="Players Online", description="")
            for player in players.players:
                embed.add_field(name=player.name, value= str(int(player.duration / 60)) + " mins" , inline=True)
            await client.send_message(message.channel, embed=embed)
