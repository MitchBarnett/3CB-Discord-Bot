import json

def read():
    try:
        with open("config.json") as configFile:
            config = json.load(configFile)
    except FileNotFoundError:
        print("Config file not found")
        print("Exiting")
        raise SystemExit
    except json.decoder.JSONDecodeError:
        print("Error in config file")
        print("Exiting")
        raise SystemExit

    return config

def getValue(key):
    config = read()
    try:
        return config[key]
    except KeyError:
        print("'%s' not found in config file" % str(key))
