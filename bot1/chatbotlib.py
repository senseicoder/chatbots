from flask import Flask, request, json, jsonify
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
