#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
import oauth2 as oauth
import urllib
import json
from google.appengine.ext import webapp  
from google.appengine.ext.webapp.util import run_wsgi_app  
 

msg=""

logging.getLogger().setLevel(logging.DEBUG)
 
class MainPage(webapp.RequestHandler):    
   def get(self):
      global msg 
      msg = self.request.get("msg")
      self.response.headers['Content-Type'] = 'text/plain'      
      self.response.out.write('Hello World!')  

   def post(self):
      global msg
      msg = self.request.body

application = webapp.WSGIApplication([('/',MainPage)],                                       
                                     debug=True)
run_wsgi_app(application)


# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key="290558b90c73178eb853f3ffad5abd3d", secret="218315233fa1920d5b55a7e517a36340")
token = oauth.Token(key="1383854-7b49be3218498d43cb24cf4e516b17c7", secret="9c40834c89bcc9a45ec65bb798ab3c24")
# Request token URL for Twitter.
#request_token_url = "http://api.fanfou.com/account/notification.json"

post_url = "http://api.fanfou.com/statuses/update.json"

# Create our client.
client = oauth.Client(consumer, token)

# The OAuth Client request works just like httplib2 for the most part.

root=json.loads(msg)

message=""
timestamp=""

logging.debug(root)

if "commits" in root:
    for commits in root["commits"]:
        if "message" in commits:
            message = commits["message"]

        if "timestamp" in commits:
            timestamp = commits["timestamp"]
            y = timestamp.split("T")[0]
            d = timestamp.split("T")[1].split("+")[0]
            timestamp = y+" "+d

        msg="["+ timestamp + "] [ Project WUNDER ]:"+message

        body = {"status": msg.encode("utf-8"),}
        form_data = urllib.urlencode(body)
        resp, content = client.request(post_url, "POST", form_data)
#print resp
#print content
