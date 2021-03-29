#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

import os, sys, getopt
import re
from flask import Flask, request, json


app = Flask(__name__)
rexec2 = re.compile(r'^ec2 ls$')

@app.route('/', methods=['POST'])
def on_event():
  """Handles an event from Google Chat."""
  event = request.get_json()
  print(event)
  if event['type'] == 'ADDED_TO_SPACE' and 'singleUserBotDm' not in event['space']:
    text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
  elif event['type'] == 'MESSAGE':
    text = 'You said: `%s` on `%s`' % (event['message']['text'], event['space']['name'])
#    if event['message']['text'] == 'ec2 ls':
#        text = 'on va essayer'
#    else:
#        text = 'je n\'ai pas compris'
  else:
    return
  return json.jsonify({'text': text})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True, ssl_context=('/etc/letsencrypt/live/bots.plcoder.net/fullchain.pem', '/etc/letsencrypt/archive/bots.plcoder.net/privkey1.pem'))
