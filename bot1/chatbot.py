from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

authfile = None

def init(authfile_):
	global authfile
	authfile = authfile_

def sendmsg(space, event, msg, classe):
  scopes = 'https://www.googleapis.com/auth/chat.bot'
  credentials = ServiceAccountCredentials.from_json_keyfile_name(authfile, scopes)
  chat = build('chat', 'v1', http=credentials.authorize(Http()))
  resp = chat.spaces().messages().create(
    parent=space, # use your space here
    body={'text': '('+event+') '+msg}).execute()
  return resp
