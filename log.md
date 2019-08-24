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