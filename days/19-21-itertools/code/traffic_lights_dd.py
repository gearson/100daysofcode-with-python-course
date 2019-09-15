#%%
import itertools

import time
import random

#%%
colors = itertools.cycle(['Red', 'Amber', 'Green', 'Amber'])
                          
while True:
    for color in colors:
        if color == 'Red':
            print(f'The light is {color}.')
            delay = random.randint(1,5)
            time.sleep(delay) 

        elif color == 'Green':
            print(f'The light is {color}.')
            delay = random.randint(1,5)
            time.sleep(delay) 

        else:
            print(f'The light is {color}.')
            time.sleep(2) 

#%%
