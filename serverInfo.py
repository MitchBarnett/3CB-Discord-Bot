import valve.source.a2s
import config
def getQueryAdress():
    ip = str(config.getValue("serverIP"))
    port = int(config.getValue("serverPort")) + 1 # query port is +1
    return (ip, port)
def getInfo():
    with valve.source.a2s.ServerQuerier(getQueryAdress()) as server:
        return server.info()
def getPlayers():
    with valve.source.a2s.ServerQuerier(getQueryAdress()) as server:
        return server.players()
