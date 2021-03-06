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
        if message.content.lower().startswith("!mission"):
            info = serverInfo.getInfo()
            if info is None:
                await client.send_message(message.channel, "The server is currently offline")
            else:
                await client.send_message(message.channel, "The current mission is %s on %s" % (info.game, info.map))

        elif message.content.lower().startswith("!players"):
            info = serverInfo.getInfo()
            if info is None:
                await client.send_message(message.channel, "The server is currently offline")
            else:
                await client.send_message(message.channel, "There is currently %i players online" % info.player_count)

        elif message.content.lower().startswith("!who"):
            players = serverInfo.getPlayers()
            if players is None:
                await client.send_message(message.channel, "The server is currently offline")
            else:
                embed = discord.Embed(title="Players Online", description="")
                for player in players.players:
                    embed.add_field(name=player.name, value= str(int(player.duration / 60)) + " mins " + str(player.score), inline=True)
                await client.send_message(message.channel, embed=embed)
        
        elif message.content.lower().startswith("!gettingstarted") or message.content.lower().startswith("!quickstart"):
            steps = ("1. Download and install [TeamSpeak 3](https://www.teamspeak.com/teamspeak3)\n"
                    "2. Download and install [Arma3Sync](http://www.armaholic.com/page.php?id=22199).\n"
                    "3. Within Arma3Sync create a new repository using the auto-config url: http://repo.3commandobrigade.com/autoconfig\n"
                    "4. Select and connect to the \"Public Modset\"\n"
                    "5. Check for addons then select all addons and download\n"
                    "6. With TS3 Closed run the TFAR Installer in the \"@task_force_radio\\teamspeak\" folder\n"
                    "7. Connect to the 3CB Team Speak Server: voice.3commandobrigade.com\n"
                    "8. Use Arma3Sync to start ArmA and connect to the Public Server\n\n"
                    "For a full guide [watch our video tutorial](https://www.youtube.com/watch?v=s7bxlUjmrc4)")
            embed = discord.Embed(title="Overview of Steps to get you up and running", description=steps, url="https://www.3commandobrigade.com/viewtopic.php?f=57&t=1765&p=13754" )
            await client.send_message(message.channel, embed=embed)

        elif message.content.lower().startswith("!optimes"):
            steps = ("__**Public:**__\n"
                    "The public server runs missions 24/7 using ALIVE \n"
                    "Missions are rotated on Wednesday and Sunday Nights\n"
                    "Zeus Open Event: Last Friday of the month 20:00\n"
                    "__**Private Operations:**__\n"
                    "Sunday Private Op: 19:30\n"
                    "Wednesday Mid-Week Op: 19:30\n"
                    "Friday Patrol Op: 20:00")
            embed = discord.Embed(title="3CB Standard Operation Times", description=steps)
            embed.set_footer(text="All times in GMT")
            await client.send_message(message.channel, embed=embed)
