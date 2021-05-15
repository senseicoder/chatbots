#!/usr/bin/env python3

#docs
#https://daemonize.readthedocs.io/en/latest/
#https://stackoverflow.com/questions/6337119/how-do-you-daemonize-a-flask-application

from flask import Flask, request, json, jsonify

import os, sys, getopt
import re
import sys

import log
import chatbotlib

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def on_event_test():
    return 'ok'

@app.route('/simple', methods=['POST'])
def on_event():
  data = request.get_json(force=True)
  addlog("envoi " + data['msg'])
  sendmsg(data['event'], data['msg'], data['classe'])
  return 'sent'

def main():
  log.addlog("demarrage avec toutes les infos de la conf")
  app.run(host='0.0.0.0', port=8001, debug=True)
  log.addlog("apres flask")
  #, ssl_context=('/etc/letsencrypt/live/bots.plcoder.net/fullchain.pem', '/etc/letsencrypt/archive/bots.plcoder.net/privkey1.pem')

if __name__ == '__main__':
  main()
