#%%
from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests
#%%

names = 'deniz rebecca max sieglinde can sven'.split()

for name in names:
    print(name.title())
#%%
first_half_alphabet = list(string.ascii_lowercase)[:13]
first_half_alphabet

#%%
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
new_names

#%%
new_names = [name.title() for name in names if name[0] in first_half_alphabet]
new_names

#%%
resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()

words[:5]
#%%
cnt = Counter(words)
cnt.most_common(5)
#%%
words = [re.sub(r'\W+', r'', word) for word in words]

#%%
resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
len(stopwords)

#%%
words = [word for word in words if word.strip() and word not in stopwords]

#%%
