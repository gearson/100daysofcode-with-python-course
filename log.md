# 100 Days Of Code - Log

## Day 1: 19/08/19

**Work Log.** Worked on day 1 of the course. Some refresh on datetime stuff.

**Thing's I've learned.** You can add timedelta objects to datetime objects.  
> datetime.today + timedelta(hours = 5)  

Gives you the current time + the timedelta time 

With str() this formats to a nice readable format! Useful for log files.

* timedelta can be decoded into days and seconds (t.days, t.seconds), not hours!  
* overcome this issue by t.seconds / 60 / 60

## Day 2: 19/08/20

**Work Log.** Pybite 67, 128 & 7

**Thing's I've learned.** 
* Use end_date.strftime('%Y-%m-%d') to format datetime object. This will return the date with the yyyy-mm-dd format!

* Use datetime.strptime() to convert a string to a datetime object

> eu_date = datetime.strptime(date, '%d/%m/%Y')  
> us_date = eu_date.strftime('%m/%d/%Y')  

* recap pybite 7. With line.split()[1] you split a string into a list where each word is an element in the list. In the pybite the dates where always the second 'word' in the string.

## Day 3: 19/08/21

**Work log.** Made a pomodoro timer.

**Thing's I've learned.**  
* learned avout f strings! Super useful. 
> f'Example text with a {variable}!'.  

* also read up a bit on \_\_name__=='\_\_main__'   
**Still not sure what exactly it does!**

## Day 4: 19/08/22

**Work log.** Day 4 of the course. Video lessons on collections

**Thing's I've learned.** 
* Apparently it is common to use spaces around '=' for variable assignments, but not for keyword arguments...  
* namedtuples make code more readable! user.name is easier to make sense of than user[0]  
* Use **defaultdict** to initialize a dictionary with a type (e.g. *defaultdict(list)*)  
* dictionaries return a keyerror, if you try to get an item with a key that is not currently in the dictionary. defauldict will simply create any items you try to access and don't exist, yet. It uses the given argument to create that default item (e.g. list)

> Counter(list).most_common(5)  

Super useful!!!

* conventional to use _ for throwaway variables
* deque is a faster alternative to lists, if we need to remove at both ends of a collection

## Day 5: 19/08/23

**Work log.** Mostly worked on visualizations for a statistics presentation to illustrate how the Central Limit Theorem works. So working with np.rand and sample to generate random numbers and then sample from them.  
For the #100days course I looked at the day 5 content, but did not fully get the code of the challenge. Will work through it before tackling the day 6 content.

**Thing's I've learned.** Took me a while to figure out why urlretrieve worked. The movies csv was saved in the first folder level...  

## Day 6: 19/08/24

**Work log.** Worked a bit more on collections and on understanding them properly.
Also looked more in depth of the day 5 content.

**Thing's I've learned.**   

    with open("x.txt") as f:  
        data = f.read()  
        do something with data

This will open a file and make sure it is closed.

From day 5:

    def get_movies_by_director(data=movies_csv):

        directors = defaultdict(list)
        with open(data, encoding='utf-8') as f:
            for line in csv.DictReader(f):
                try:
                    director = line['director_name']
                    movie = line['movie_title'].replace('\xa0', '')
                    year = int(line['title_year'])
                    score = float(line['imdb_score'])
                except ValueError:
                    continue

                m = Movie(title=movie, year=year, score=score)
                directors[director].append(m)

        return directors

The Output of each line from DictReader is:
>OrderedDict([('color', 'Color'), ('director_name', 'Jon Gunn'), ('num_critic_for_reviews', '43') ... etc. ])

**Absolutely revisit pybite 13**  
Also check pybite solutions 001, 021, 023, 034, 036, 042, 045, 055, 057, 063, 076, 084, 086, 095, 096 on https://github.com/pybites/100DaysOfCode/blob/master/LOG.md

## Day 7: 19/08/25

**Work log.** Just day 7 videos and a bit messing around on data structures.

**Thing's I've learned.** Refreshed mainly on some list methods like reverse, sort.  
* list(str) to make a list of characters from a string.  
* list.pop() to get last character in a list.  
* list.insert(idx, x) to insert x at index.  
* l.append() to add to the last position of a list.  

## Day 8: 19/08/26

**Work log.** Recapped some of the videos for day 7 and 8, recapped how to handle csvs with a Corey Schaefer video and completed Pybite 21.

**Thing's I've learned.** 
Again worked through this syntax to read csv files:  

    with open(filename, 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       for line in csv_reader:
           print(line)    

Leaving this here now, since there will be a csv module on day 37-39 of this course.  
Also got reminded that I need this syntax when I want to loop over a dictionary:  
> for key, value in dictionary.**items()**  

And use ', '.join(list) to join elements of a list to a single string with the given delimiter!  

## Day 9: 19/08/27

**Work log.** Started on pybite 89 and did some EDA stuff.


## Day 10: 19/08/28

**Work log.** Completed pybite 89 and started on videos for day 10.

**Thing's I've learned.** 
> sorted(list, key = lambda k: len(k))[-1]

This takes a list, lambdas through it and assigns each element a key with it's length. It then sorts them and here  we take the last one.

## Day 11: 19/08/29

**Work log.** Mostly some eda stuff.

**Thing's I've learned.** I learned a some new stuff about plotting and this fig, ax = subplot() syntax.  
Don't forget that dicts are unordered.  

## Day 12: 19/08/30

**Work log.** Finished all videos of the testing block and played around a bit.

**Thing's I've learned.** Intro to testing. **Will revisit testing at a later date!**  
Also checkout https://pybit.es/pytest-fixtures.html

## Day 13: 19/09/01

**Work log.** Read up on venv and tested it a bit. https://docs.python.org/3/tutorial/venv.html

**Thing's I've learned.** Learned how to use venv on windwos and WSL.

## Day 14: 19/09/02

**Work log.** Text game videos (day 13-15). Coded along

**Thing's I've learned.** Learned about classes, __init__, add behaviors with def

## Day 15: 19/09/03

**Work log.** Started on the rock, paper, scissors game.

**Thing's I've learned.** Practicing how classes work. Not sure yet what this self really does.

## Day 16: 19/09/04

**Work log.** Worked on setting up zsh...

**Thing's I've learned.** Figured some stuff out about zsh and themes. Nothing too productive...

## Day 17: 19/09/05

**Work log.** Started on day 16 and 17 content. Still need to catch up with the rock, paper, scissors game, though. 

**Thing's I've learned.** Learned mostly about list comprehensions and generators.  
'string'.title() to capitalize first letter.
Groupby two columns and only take the first of the duplicates
> df_filtered = df.groupby(['UserId', 'DisplayTime']).head(1)

> df_combis.columns[(df_combis == 1).iloc[i]]

Used this for a problem today:
action_dict = [{df_combis.index[i] : tuple(df_combis.columns[(df_combis == 1).iloc[i]])} for i in range(30)]

> words = [word for word in words if word.strip() and word not in stopwords]  

If word.strip() to check for empty strings. If we check for word.strip()==True we discard empty strings

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

Generators are faster. They are yielding one by one lazyly.

## Day 18: 19/09/06

**Work log.** Finished list comprehension and generator exercises. Implemented generators consciously during work, too.

**Thing's I've learned.** Learned more about how to use generators. With itertools.islice I can also chose iterations for a generator.