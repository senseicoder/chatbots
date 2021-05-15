#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

import sys

import yaml
config = yaml.safe_load(open("config.dev.yml"))
#print(yaml.dump(config))

import log
log.init(config['daemon']['pid'], config['daemon']['log'])

import chatbot
chatbot.init(config['googlechat']['authfile'])

log.add("envoi " + sys.argv[2])
resp = chatbot.sendmsg(sys.argv[1], 'CRITICAL', sys.argv[2], 'perso')
print(resp)