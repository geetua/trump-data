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
curl $SPEECHES | OUT=/tmp/speeches ./bin/dl.py
```

Then clean it

```
mkdir -p /tmp/cleaned/speeches
for file in `ls /tmp/speeches`; do
  echo $file
  ./bin/clean.py < /tmp/speeches/$file > /tmp/cleaned/speeches/$file
done
pushd /tmp/cleaned/speeches
rename "s/html/json/" *.html
popd
```

And repeat for any other candidate / content type you want. See: http://www.presidency.ucsb.edu/2016_election.php

Examples
--------

After Trump secured the nomination, the campaign relied only on speeches

![trump-communication.png](examples/trump-communication.png)

Whereas Clinton had a more even distribution of speeches, press releases, and statements

![clinton-communication.png](examples/clinton-communication.png)

This shows the lexical dispersion plot for several phrases in all of Trump's speeches concatenated together

![trump-lexical-dispersion-plot.png](examples/trump-lexical-dispersion-plot.png)

Some notable features include

* Jobs and trade were mentioned constantly throughout the speeches, but economy less so
* Sanders was discussed briefly at the beginning, then brought up again at the end
* There was a segment in the speeches that heavily focused on ISIS, but it was relatively low frequency overall
* Immigration had a similar bursty pattern, but was a more heavy focus overall than ISIS
* Obamacare increased in frequency of mentions towards the end of the speeches
* "Crooked" (to describe Clinton), was used only a few times towards beginning of speeches (though anecdotally, this appears seemingly more often in Tweets - should follow up on that)
