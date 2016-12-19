#!/usr/bin/env python
#
# Prepare: 
# START_TIME=2015-01-01 ./analysis/concat-tweets.py < data/2016_donald-trump/tweets/donald-trump-tweets.csv | iconv -f utf-8 -t ascii//translit > /tmp/trump-tweets.txt 
#
import csv
import os
import fileinput
import sys

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

start_time = os.environ.get('START_TIME', '2000-01-01')

reader = csv.reader(fileinput.input())

tweets = []

for row in reader:
    # (date, text)
    if row[0] == 'Text':
        continue # header
    tweets.append((row[1], row[0]))

for tweet in sorted(tweets):
    if tweet[0] >= start_time:
        sys.stdout.write(tweet[1])
        sys.stdout.write("\n")
