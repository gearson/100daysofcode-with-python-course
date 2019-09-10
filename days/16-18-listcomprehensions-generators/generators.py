#%%
from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

#%%
def num_gen():
    for i in range(5):
        yield i

gen = num_gen()

#%%
next(gen)

#%%
for i in gen:
    print(i)

#%%
options = 'red yellow blue white black green purple'.split()
options

#%%
def create_select_options_gen(options=options):
    for option in options:
        yield f'{option.title()}'

#%%
create_select_options_gen()

#%%
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
        return leap_years

def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year

#%%
%timeit -n1 leap_years_lst()
#%%
%timeit -n1 leap_years_gen()

