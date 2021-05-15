#!/usr/bin/env python3

#docs
#https://daemonize.readthedocs.io/en/latest/
#https://stackoverflow.com/questions/6337119/how-do-you-daemonize-a-flask-application

import os, sys, getopt
import re
from flask import Flask, request, json, jsonify

import sys
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

from datetime import datetime
import logging
#from daemonize import Daemonize

def sendmsg(event, msg, classe):
  scopes = 'https://www.googleapis.com/auth/chat.bot'
  credentials = ServiceAccountCredentials.from_json_keyfile_name('/space/etc/google_api/chatbot1.json', scopes)
  chat = build('chat', 'v1', http=credentials.authorize(Http()))
  resp = chat.spaces().messages().create(
    parent='spaces/sCD2iwAAAAE', # use your space here
    body={'text': '('+event+') '+msg}).execute()
  print(resp)

pid = "/var/run/passchat.pid"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("/var/log/passchat.log", "a")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]

def addlog(line):
  global logger
  logger.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + line)

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
  addlog("demarrage avec toutes les infos de la conf")
  app.run(host='0.0.0.0', port=8001, debug=True)
  addlog("apres flask")
  #, ssl_context=('/etc/letsencrypt/live/bots.plcoder.net/fullchain.pem', '/etc/letsencrypt/archive/bots.plcoder.net/privkey1.pem')

if __name__ == '__main__':
  #daemon = Daemonize(app="passchat", pid=pid, action=main, keep_fds=keep_fds)
  #daemon.start()
  main()
