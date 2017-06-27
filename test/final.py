#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/zen/Workspace/src/fanfou")
import oauth2 as oauth
import urllib


# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key="290558b90c73178eb853f3ffad5abd3d", secret="218315233fa1920d5b55a7e517a36340")
token = oauth.Token(key="1383854-7b49be3218498d43cb24cf4e516b17c7", secret="9c40834c89bcc9a45ec65bb798ab3c24")
# Request token URL for Twitter.
#request_token_url = "http://api.fanfou.com/account/notification.json"

post_url = "http://api.fanfou.com/statuses/update.json"

# Create our client.
client = oauth.Client(consumer, token)

# The OAuth Client request works just like httplib2 for the most part.


msg=sys.argv[1]
print msg

body = { 
		"status": msg,
		}
form_data = urllib.urlencode(body)

resp, content = client.request(post_url, "POST", form_data)
print resp
print content
