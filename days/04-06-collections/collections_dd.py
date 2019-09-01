#%% 
from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
#%%
# namedtuple
# used to define a class without methods
# allows to store dict like object you can access by attributes

user = ('bob', 'coder')
f'{user[0]} is a {user[1]}'
#%%
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')
user.name

#%%
f'{user.name} is a {user.role}'
# named tuples make code more readable!

#%%
users = {'bob' : 'coder'}
users['bob']
#%%
users['julian']  # returns a key error
#%%
users.get('bob')

#%%
# what if you need to build up a collection?
challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
challenges_done

#%%
challenges = {}
for name, challenge in challenges_done:
    challenges[name].append(challenge)

#%%
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
challenges

#%%
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
words[:5]

#%%
Counter(words).most_common(5)

#%%
lst = list(range(10000000))
deq = deque(range(10000000))

#%%
def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

%timeit insert_and_delete(lst)

%timeit insert_and_delete(deq)

#%%
