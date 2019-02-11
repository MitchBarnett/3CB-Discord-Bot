import valve.source.a2s
import config
def getQueryAdress():
    ip = str(config.getValue("serverIP"))
    port = int(config.getValue("serverPort")) + 1 # query port is +1
    return (ip, port)
def getInfo():
    try:
        with valve.source.a2s.ServerQuerier(getQueryAdress()) as server:
            return server.info()
    except valve.source.util.NoResponseError:
        return None
def getPlayers():
    try:
        with valve.source.a2s.ServerQuerier(getQueryAdress()) as server:
            return server.players()
    except valve.source.util.NoResponseError:
        return None
