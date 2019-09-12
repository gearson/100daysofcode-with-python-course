#%%
number = list(range(1,11))

for i in number:
    print(i)

#%%
it = iter('string')
next(it)
#%%
import itertools
import sys
import time
#%%
symbols = itertools.cycle('-\|/')

while True:
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush()
    time.sleep(0.08)

#%%
from itertools import product

#%%

for letter in product('rebecca', repeat=2):
    print(letter)

#%%
from itertools import permutations, combinations

#%%
friends = 'mike bob julian'.split()

friends

#%%
print(list(combinations(friends, 2)))

#%%
print(list(permutations(friends, 2,)))

#%%
