#!/usr/bin/env python
import sys
import json

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

texts = []

for filename in sys.argv[1:]:
    with open(filename) as f:
        texts.append(json.loads(f.read())['text'])

print '\n'.join(texts)
