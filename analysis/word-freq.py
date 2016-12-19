#!/usr/bin/env python
#
# Prepare: ./analysis/concat-text.py data/2016_donald-trump/speeches/* > /tmp/all-trump.txt
#
import sys
import nltk
import string
from nltk.corpus import stopwords

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

# Load data
raw = sys.stdin.read()
tokens = nltk.word_tokenize(raw)

# With stopwords / punctuation removed
trans = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
stops = set(stopwords.words('english'))
filtered_tokens = map(lambda x: x.translate(trans), tokens)
filtered_tokens = [word for word in filtered_tokens if word not in stops]
text = nltk.Text(filtered_tokens)

# Word length
fdist = nltk.FreqDist(len(w) for w in text)
fdist.most_common()
"""
Trump:
1,18375
5,13886
4,13790
7,12204
6,11256
3,8495
8,8336
9,5593
2,5037
10,3353
11,2272
12,1131
13,905
14,575
15,324
16,308
17,167
18,94
19,41
20,32
21,21
22,14
24,9
23,5
27,2
28,2
25,1
26,1

Clinton:
1,104019
4,77296
5,62560
6,54570
7,51560
3,48893
8,36058
2,28362
9,26419
10,15759
11,8093
12,4650
13,3102
14,1908
15,663
16,525
17,250
18,223
19,83
20,46
21,27
22,25
24,14
23,9
29,3
25,2
26,2
27,2
28,2
33,2
30,1

"""

"""
Combined, with weighted (total clinton words 525128, trump 106229)

letters,candidate,count,weighted
2,clinton,28362,0.0540096890663
2,trump,5037,0.0474164305416
3,clinton,48893,0.0931068234792
3,trump,8495,0.0799687467641
4,clinton,77296,0.147194588748
4,trump,13790,0.129813892628
5,clinton,62560,0.119132859036
5,trump,13886,0.130717600655
6,clinton,54570,0.103917521062
6,trump,11256,0.105959766166
7,clinton,51560,0.0981855852287
7,trump,12204,0.114883882932
8,clinton,36058,0.0686651635411
8,trump,8336,0.0784719803444
9,clinton,26419,0.0503096387928
9,trump,5593,0.0526504061979
10,clinton,15759,0.0300098261757
10,trump,3353,0.031563885568
11,clinton,8093,0.0154114806295
11,trump,2272,0.021387756639
12,clinton,4650,0.00885498392773
12,trump,1131,0.0106468101931
13,clinton,3102,0.00590713121372
13,trump,905,0.00851933087952
14,clinton,1908,0.0036333998568
14,trump,575,0.00541283453671
15,clinton,663,0.00126254932131
15,trump,324,0.00305001459112
16,clinton,525,0.000999756249905
16,trump,308,0.00289939658662
17,clinton,250,0.000476074404717
17,trump,167,0.00157207542197
18,clinton,223,0.000424658369007
18,trump,94,0.000884880776436
19,clinton,83,0.000158056702366
19,trump,41,0.000385958636531
20,clinton,46,8.75976904678e-05
20,trump,32,0.000301236008999
21,clinton,27,5.14160357094e-05
21,trump,21,0.000197686130906
22,clinton,25,4.76074404717e-05
22,trump,14,0.000131790753937
23,clinton,9,1.71386785698e-05
23,trump,5,4.70681264062e-05
24,clinton,14,2.66601666641e-05
24,trump,9,8.47226275311e-05
25,clinton,2,3.80859523773e-06
25,trump,1,9.41362528123e-06
26,clinton,2,3.80859523773e-06
26,trump,1,9.41362528123e-06
27,clinton,2,3.80859523773e-06
27,trump,2,1.88272505625e-05
28,clinton,2,3.80859523773e-06
28,trump,2,1.88272505625e-05
29,clinton,3,5.7128928566e-06
29,trump,0,0
30,clinton,1,1.90429761887e-06
30,trump,0,0
33,clinton,2,3.80859523773e-06
33,trump,0,0
"""

# Collocations
colloc = text.collocations()
"""
Trump:

Hillary Clinton; United States; Donald Trump;  re going; Make America;
Middle East; special interests; New York; inner cities; trade deals;
President Obama; school choice; law enforcement; repeal replace;
cheers applause; Wall Street; Secretary State; November 8th; Supreme
Court; Trump Administration

Clinton:

re going; United States; health care; Hillary Clinton; New York;
Donald Trump;  ve got; White House; middle class; make sure; Wall
Street; New Hampshire; every single; want thank; young people; men
women; Middle East; Social Security; President Obama; Senator Obama

"""

