#!/usr/bin/env python
#
# Prepare: ./analysis/concat-text.py data/2016_donald-trump/speeches/* > /tmp/all-trump.txt
# Run: ./analysis/trump-lexical-dispersion-plot.py < /tmp/all-trump.txt
#
import sys
import nltk

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

raw = sys.stdin.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
nltk.draw.dispersion_plot(text, [
    "isis",
    "mexico",
    "wall",
    "immigration",
    "obamacare",
    "crooked",
    "hillary",
    "bernie",
    "obama",
    "rigged",
    "law",
    "order",
    "economy",
    "jobs",
    "trade",
], 
ignore_case=True,
title='Lexical Dispersion Plot of Select Phrases in Time-Ordered Trump Speeches')
