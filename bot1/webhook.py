#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

import os, sys, getopt
import re
from flask import Flask, request, json, jsonify

import sys
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

def sendmsg(event, msg, classe):
  scopes = 'https://www.googleapis.com/auth/chat.bot'
  credentials = ServiceAccountCredentials.from_json_keyfile_name('/space/etc/google_api/chatbot1.json', scopes)
  chat = build('chat', 'v1', http=credentials.authorize(Http()))
  resp = chat.spaces().messages().create(
    parent='spaces/sCD2iwAAAAE', # use your space here
    body={'text': '('+event+') '+msg}).execute()
  print(resp)

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def on_event_test():
    return 'ok'

@app.route('/simple', methods=['POST'])
def on_event():
  """Handles an event from Google Chat."""
  #return jsonify(request.form.to_dict(flat=False))
  data = request.get_json(force=True)
  sendmsg(data['event'], data['msg'], data['classe'])
  return 'ok'
  #sendmsg(event=, msg=a['msg'])
  #return request.form.get("msg")
  #event = request.json()
  #dump(request)
  #return 'ok'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8001, debug=True)
  #, ssl_context=('/etc/letsencrypt/live/bots.plcoder.net/fullchain.pem', '/etc/letsencrypt/archive/bots.plcoder.net/privkey1.pem')
