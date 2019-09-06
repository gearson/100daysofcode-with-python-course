#%%
from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

#%%
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

#%%
[name.title() for name in NAMES]

#%%
def split_reverse(name):
    first_name, last_name = name.title().split(' ')
    return f'{last_name} {first_name}'
#%%
[split_reverse(name) for name in NAMES]

#%%
def gen_pairs(NAMES):
    first_names = [name.title().split(' ')[0] for name in NAMES]
    first = random.choice(first_names)
    first_names.remove(first)
    second = random.choice(first_names)
    return f'{first} pairs up with {second}'
    

#%%
[gen_pairs() for _ in range(20)]

#%%
def gen_pairs(NAMES = NAMES):
    first_names = [name.title().split(' ')[0] for name in NAMES]
    first, second = random.sample(first_names,2)
    return f'{first} pairs up with {second}'

#%%
pairs = gen_pairs()
first_ten = itertools.islice(pairs, 10)
list(first_ten)

#%%
