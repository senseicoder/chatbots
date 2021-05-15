#!/usr/bin/env python3

#docs
#https://daemonize.readthedocs.io/en/latest/
#https://stackoverflow.com/questions/6337119/how-do-you-daemonize-a-flask-application

from flask import Flask, request, json, jsonify

import os, sys, getopt
import re
import sys

import yaml
config = yaml.safe_load(open("config.dev.yml"))
#print(yaml.dump(config))

import log
log.init(config['daemon']['pid'], config['daemon']['log'])
import chatbot
chatbot.init(config['googlechat']['authfile'])

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def on_event_test():
    return 'ok'

@app.route('/simple', methods=['POST'])
def on_event():
  data = request.get_json(force=True)
  log.add("envoi " + data['msg'])
  chatbot.sendmsg('spaces/sCD2iwAAAAE', data['event'], data['msg'], data['classe'])
  return 'sent'

def main():
  global config

  log.add("demarrage avec toutes les infos de la conf")

  ssl_context = None
  if config['host']['ssl']['active']:
    log.add('ssl active')
    ssl_context = (config['host']['ssl']['chain'], config['host']['ssl']['cert'])

  app.run(host=config['host']['name'], port=config['host']['port'], debug=config['host']['debug'], ssl_context=ssl_context)

if __name__ == '__main__':
  main()
