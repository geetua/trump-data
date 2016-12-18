#!/usr/bin/env python
#
# Converts a statement / press release / speech to JSON form with date, title,
# text columns
#
import sys
import os
import json
from dateutil import parser
from bs4 import BeautifulSoup

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

soup = BeautifulSoup(sys.stdin.read(), 'html.parser')

doc = {}

for displaytext in soup.find_all("span", class_="displaytext"):
    doc['text'] = displaytext.text
    break

for paperstitle in soup.find_all("span", class_="paperstitle"):
    doc['title'] = paperstitle.text
    break

for docdate in soup.find_all("span", class_="docdate"):
    doc['date'] = parser.parse(docdate.text).strftime('%Y-%m-%d')
    break

print json.dumps(doc)
