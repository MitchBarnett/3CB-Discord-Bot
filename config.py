import json
import logging

log = logging.getLogger(__name__)


def read():
    log.debug("opening config.json")
    try:
        with open("config.json") as configFile:
            config = json.load(configFile)
    except FileNotFoundError:
        log.info("Reading from config.json")
        log.critical("Config file not found")
        log.critical("Exiting")
        raise SystemExit
    except json.decoder.JSONDecodeError:
        log.critical("Error in config file")
        log.critical("Exiting")
        raise SystemExit

    return config


def getValue(key):
    log.debug("attempting to read '" + key + "' from config.json")
    config = read()
    try:
        return config[key]
    except KeyError:
        log.error("'%s' not found in config file" % str(key))
