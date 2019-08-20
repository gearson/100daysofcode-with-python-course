# 100 Days Of Code - Log

### Day 1: 19/08/19

**Work Log.** Worked on day 1 of the course. Some refresh on datetime stuff.

**Thing's I've learned.** You can add timedelta objects to datetime objects.  
> datetime.today + timedelta(hours = 5)  

Gives you the current time + the timedelta time 

With str() this formats to a nice readable format! Useful for log files.

* timedelta can be decoded into days and seconds (t.days, t.seconds), not hours!  
* overcome this issue by t.seconds / 60 / 60

### Day 2: 19/08/20

**Work Log.** Pybite 67, 128 & 7

**Thing's I've learned.** 
* Use end_date.strftime('%Y-%m-%d') to format datetime object. This will return the date with the yyyy-mm-dd format!

* Use datetime.strptime() to convert a string to a datetime object

> eu_date = datetime.strptime(date, '%d/%m/%Y')  
> us_date = eu_date.strftime('%m/%d/%Y')  

* recap pybite 7. With line.split()[1] you split a string into a list where each word is an element in the list. In the pybite the dates where always the second 'word' in the string.