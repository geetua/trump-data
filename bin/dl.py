#!/usr/bin/env python
#
# Downloads all links given a candidate page, e.g. 
# http://www.presidency.ucsb.edu/2016_election_speeches.php?candidate=45&campaign=2016TRUMP&doctype=5000
#
import requests
import sys
import os
from bs4 import BeautifulSoup
from slugify import slugify

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

soup = BeautifulSoup(sys.stdin.read(), 'html.parser')

out_dir = os.environ['OUT']

for link in soup.find_all('a'):
    href = link.get('href')
    if 'index.php' in href and 'ws' in href:
        href = href.replace('..', 'http://www.presidency.ucsb.edu')
        fname = os.path.join(out_dir, slugify(link.string) + '.html')
        print 'GET {} #=> {}'.format(href, fname)
        res = requests.get(href)
        with open(fname, 'w') as f:
            f.write(res.text)
