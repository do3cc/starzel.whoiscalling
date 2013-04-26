import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "starzel.whoiscalling",
    version='0.0.2',
    author = "Patrick Gerken",
    author_email = "gerken@patrick-gerken.de",
    description = ("Retrieve calling info from Fritzbox, expose to jabber Multi User Chatroom"),
    license = "BSD",
    long_description=read('README.rst') + read('CHANGES.rst'),
    url='https://github.com/do3cc/starzel.whoiscalling',
    keywords = "FRITZ!Box fritzbox jabber",
    packages=['starzel', 'starzel.whoiscalling'],
    install_requires = ['xmpppy', 'jabberbot'],
    entry_points = {
        'console_scripts': [
            'fritzbot = starzel.whoiscalling.bot:main']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Topic :: Communications :: Chat",
        "Topic :: Communications :: Telephony"
    ],
)
