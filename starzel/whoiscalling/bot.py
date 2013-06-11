from datetime import datetime
from jabberbot import JabberBot
from telnetlib import Telnet
import ConfigParser
import logging
import os
import re
import sys

only_number = re.compile('.*RING;\d*;(\d*);.*')

logging.basicConfig()


def run(username, password, room, fritzbox):
    logging.debug("Started at %s", datetime.now().isoformat())
    bot = JabberBot(username, password)

    telnet = Telnet(fritzbox, '1012')

    while True:
        # ugly, but seems to be the only way to stay on
        bot.join_room(room)
        logging.debug("Loop started at %s", datetime.now().isoformat())
        data = telnet.read_until('SIP0;', 300)
        number = '\n'.join(only_number.findall(data))
        if number:
            logging.debug("Sending a message at %s", datetime.now().isoformat())
            bot.send(room, "Call from " + number, message_type='groupchat')
        else:
            what = bot.conn.Process(1)
            if what != '0' and what != None:
                logging.debug("What is this %s", what)
            elif what == None:
                logging.debug("Reconnecting")
                bot.conn.reconnectAndReauth()

def main():
    config = ConfigParser.ConfigParser()
    try:
        config.read(os.path.join(os.path.expanduser('~'), '.starzelbot.cfg'))
        username = config.get('main', 'username')
        password = config.get('main', 'password')
        room = config.get('main', 'room')
        fritzbox = config.get('main', 'fritzbox')

    except:
        print("""You need a configuration files with a main section in your home directory.
It must be named .starzelbot.cfg and must contain
username = your jabber username. It must be registered already
password = your jabber password
room = your multi user room
fritzbox = your fritzbox ip. The fritzbox must have calling info activated, #96*5*""")
        sys.exit(1)

    run(username, password, room, fritzbox)
