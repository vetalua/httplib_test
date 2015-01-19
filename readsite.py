#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''This simple program read contents of sites. Use in comand line:
python readsyte.py > NAME.html to save page into file.
'''
import httplib
import sys
site = sys.argv[1]
print site
conn = httplib.HTTPConnection(site)
conn.request('GET', '/')
resp = conn.getresponse()
print resp.read()