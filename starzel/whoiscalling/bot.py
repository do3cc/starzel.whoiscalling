from jabberbot import JabberBot
from telnetlib import Telnet
import ConfigParser
import logging
import os
import sys
import re

only_number = re.compile('.*RING;\d*;(\d*);.*')

logging.basicConfig()


def run(username, password, room, fritzbox):
    bot = JabberBot(username, password)
    bot.join_room(room)

    telnet = Telnet(fritzbox, '1012')

    while True:
        data = telnet.read_until('SIP0;')
        number = '\n'.join(only_number.findall(data))
        bot.send(room, "Call from " + number, message_type='groupchat')

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
