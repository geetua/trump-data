#!/usr/bin/env python
import sys
import json

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

texts = []

for filename in sys.argv[1:]:
    with open(filename) as f:
        data = json.loads(f.read())
        texts.append((data['date'], data['text']))

for text in sorted(texts):
    print text[1]
