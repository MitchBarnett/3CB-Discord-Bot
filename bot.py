
import discord
import asyncio
import config
import serverInfo
import logging

log = logging.getLogger(__name__)


def registerCommands(client):
    @client.event
    async def on_ready():
        log.info("Running discord.py version: " + discord.__version__)
        log.info('Logged in as: ' + str(client.user))
        log.info("Running on:")
        for server in client.servers:
            log.info("%s as %s " % (server.name, server.me.display_name))

    @client.event
    async def on_message(message):
        log.debug("reading message")
        if message.content.lower().startswith("!mission"):
            log.info("!mission command received from %s on %s in #%s" %
                     (str(message.author),
                      str(message.server),
                      str(message.channel)))
            info = serverInfo.getInfo()
            if info is None:
                await client.send_message(message.channel, "The server is currently offline")
                log.info("Response: The server is currently offline")
            else:
                await client.send_message(message.channel, "The current mission is %s on %s" % (info.game, info.map))
                log.info("Response: The current mission is %s on %s" % (info.game, info.map))

        elif message.content.lower().startswith("!players"):
            log.info("!players command received from %s on %s in #%s" %
                     (str(message.author),
                      str(message.server),
                      str(message.channel)))

            info = serverInfo.getInfo()
            if info is None:
                await client.send_message(message.channel, "The server is currently offline")
                log.info("Response: The server is currently offline")
            else:
                await client.send_message(message.channel, "There is currently %i players online" % info.player_count)
                log.info("Response: There is currently %i players online" % info.player_count)

        elif message.content.lower().startswith("!who"):
            log.info("!who command received from %s on %s in #%s" %
                     (str(message.author),
                      str(message.server),
                      str(message.channel)))

            players = serverInfo.getPlayers()

            if players is None:
                await client.send_message(message.channel, "The server is currently offline")
                log.info("Response: The server is currently offline")
            else:
                embed = discord.Embed(title="Players Online", description="")
                logText = []
                for player in players.players:
                    embed.add_field(name=player.name, value= str(int(player.duration / 60)) + " mins ", inline=True)
                    logText += (player.name, str(int(player.duration / 60)) + " mins ")
                await client.send_message(message.channel, embed=embed)
                log.info("Response: " + str(logText))
        
        elif message.content.lower().startswith("!gettingstarted") or message.content.lower().startswith("!quickstart"):
            log.info("!gettingstarted command received from %s on %s in #%s" %
                     (str(message.author),
                      str(message.server),
                      str(message.channel)))


        elif message.content.lower().startswith("!optimes"):
            log.info("!optimes command received from %s on %s in #%s" %
                     (str(message.author),
                      str(message.server),
                      str(message.channel)))

            steps = ("__**Public:**__\n"
                    "The public server runs missions 24/7 using ALIVE \n"
                    "Missions are rotated on Wednesday and Sunday Nights\n"
                    "Zeus Open Event: Last Friday of the month 20:00\n"
                    "__**Private Operations:**__\n"
                    "Sunday Private Op: 19:30\n"
                    "Wednesday Mid-Week Op: 19:30\n"
                    "Friday Patrol Op: 20:00")
            embed = discord.Embed(title="3CB Standard Operation Times", description=steps)
            embed.set_footer(text="All times in BST")
            await client.send_message(message.channel, embed=embed)

    async def check_mission_change():
        await client.wait_until_ready()
        info = serverInfo.getInfo()
        channel = discord.Object(id='449340931867410474')
        if info is None:
            current_mission = "offline"
        else:
            current_mission = info.game

        while not client.is_closed:
            log.info("checking if mission has changed")
            info = serverInfo.getInfo()
            if info is None and current_mission != "offline":
                await client.send_message(channel, "The server is now offline")
                current_mission = "offline"
            elif info.game != current_mission:
                if current_mission == "offline":
                    await client.send_message(channel, "The server back online")
                await client.send_message(channel, "Mission changed to %s on %s" % (info.game, info.map))
                current_mission = info.game

            await asyncio.sleep(30)
    client.loop.create_task(check_mission_change())
