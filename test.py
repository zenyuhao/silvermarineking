#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/zen/Workspace/src/google_appengine")
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from urllib import unquote 

class UrlHandler(webapp.RequestHandler):
  def get(self, path):
    self.response.out.write(unquote(path)) # 注意要进行转义，否则输出的都是%开头的乱码

# 简单起见，我只写了一条URL映射，注意(.*)会被传递到UrlHandler.get的path参数中
application = webapp.WSGIApplication([('/(.*)', UrlHandler),])

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
