starzel.whoiscalling
====================

Small bot that monitors your FRITZ!Box for incoming calls and informs
a multiuserchat in jabber.

How to use
----------
For this to work, it needs a bunch of configuration options. The script needs a configuration file in ~/starzelbot.cfg.
The configuration needs a main section.
This is how a sample configuration could look like::

    [main]
    username = mybot@jabber.ccc.de
    password = xxx
    room = yourgroup@conference.jabber.ccc.de
    fritzbox = 192.168.1.1

The egg exposes a script called `fritzbot`. The `fritzbot` script does not accept any parameters, and it blocks. If you want to run it in the background, start it with nohup.

In normal operation, the script generates no output. So it should be save to start it via cron.

What does it do
---------------

A FRITZ!Box with VoIP offers an interface to get informed of incoming calls.

This information gets exposed via a simple interface accessible on the FRITZ!Box at port 1012

This bot connects to this port on the FRITZ!Box and tries to extract the caller.

For each call, it sends a message to a multi user chatroom on jabber.

