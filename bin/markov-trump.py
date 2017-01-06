#!/usr/bin/env python
#
# Reads a CSV of tweets, and generates some more
#
# E.g. COUNT=1 ./bin/markov-trump.py < data/2016_donald-trump/tweets/donald-trump-tweets.csv
#
import csv
import markovify
import os
import sys

count = int(os.getenv('COUNT', '5'))

text = ''.join(map(lambda x: x[0], csv.reader(sys.stdin)))

text_model = markovify.Text(text)

for i in range(count):
    print(text_model.make_short_sentence(140))
