starzel.whoiscalling
====================

Small bot that monitors your fritzbox for incoming calls and informs
a multiuserchat in jabber.

A Fritz!box with VoIP offers an interface to get informed of incoming calls.

This information gets exposed via a simple interface accessible on the Fritz!box at port 1012

This script connects to this port on the Fritz!Box and tries to extract the caller.

For each call, it sends a message to a multi user chatroom on jabber.

For this to work, it needs a bunch of configuration options. The script needs a configuration file in ~/starzelbot.cfg.
The configuration needs a main section.
This is how a sample configuration could look like:

[main]
username = mybot@jabber.ccc.de
password = xxx
room = yourgroup@conference.jabber.ccc.de
fritzbox = 192.168.1.1
