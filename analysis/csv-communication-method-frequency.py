#!/usr/bin/env python
import sys
import json
import os

rows = []

for method in os.listdir(sys.argv[1]):
    dirname = os.path.join(sys.argv[1], method)
    for filename in os.listdir(dirname):
        with open(os.path.join(dirname, filename)) as f:
            data = json.loads(f.read())
            rows.append((data['date'], method))

print 'date,method'
for row in sorted(rows):
    print '{},{}'.format(row[0], row[1])
