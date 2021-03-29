#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

import sys
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
scopes = 'https://www.googleapis.com/auth/chat.bot'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
            '/space/etc/google_api/chatbot1.json', scopes)
chat = build('chat', 'v1', http=credentials.authorize(Http()))
resp = chat.spaces().messages().create(
            parent=sys.argv[1], # use your space here
                body={'text': sys.argv[2]}).execute()
print(resp)

