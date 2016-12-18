trump-data
==========

Source: http://www.presidency.ucsb.edu/2016_election.php

Each JSON file has three columns:

* date - Date speech / statement / press release was made
* title - Title as given by UCSB
* text - Text of speech stripped of HTML tags

Run
---

First download the data

```
SPEECHES="http://www.presidency.ucsb.edu/2016_election_speeches.php?candidate=45&campaign=2016TRUMP&doctype=5000"
mkdir /tmp/speeches
curl $SPEECHES | OUT=/tmp/speeches ./dl.py
```

Then clean it

```
mkdir /tmp/cleaned/speeches
for file in `ls /tmp/speeches`; do
  echo $file
  ./clean.py < /tmp/speeches/$file > /tmp/cleaned/speeches/$file
done
```
