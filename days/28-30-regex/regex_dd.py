#%%
import re

text = 'Awesome, I am doing the #100DaysOf Code challenge after all'

#%%
re.search(r'I am',text)

#%%
re.match(r'I am', text)

#%%
re.findall(r'\w+',text)

#%%

re.findall(r'[A-Z][a-z0-9]+', text)

#%%
from collections import Counter

cnt = Counter(re.findall(r'[A-Z][a-z0-9]+', text))
cnt.most_common()

#%%
re.findall(r'a[a-z0-9]+', text)

#%%
movies = '''1. Citizen Kane (1941),
2. The Godfather (1972),
3. Casablanca (1942),
4. Raging Bull (1980),
5. Singin' in the Rain (1952),
6. Gone with the Wind (1939),
7. Lawrence of Arabia (1962),
8. Schindler's List (1993),
9. Vertigo (1958),
10. The Wizard of Oz (1939)'''.split('\n')
movies

#%%
pat = re.compile(r'''
                 ^
                 \d+
                 \.
                 \s+
                 (?:
                 [A-Za-z']+\s
                 )
                 {2}
                 \(
                \d{4}
                \)
                $                 
                 ''',re.VERBOSE)

#%%
for movie in movies:
    print(movie, pat.match(movie))

#%%
text = 'Awesome, I am doing the #100DaysOfPython Code challenge after all 2 200 400'
re.sub(r'\d+', '100', text)

#%%
re.sub(r'(#\d+DaysOf)\w+', r'\1Test', text)

#%%
