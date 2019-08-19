# 100 Days Of Code - Log

### Day 1: 19/08/19

**Work Log.** Worked on day 1 of the course. Some refresh on datetime stuff.

**Thing's I've learned.** You can add timedelta objects to datetime objects.  
> datetime.today + timedelta(hours = 5)  

Gives you the current time + the timedelta time 

With str() this formats to a nice readable format! Useful for log files.

* timedelta can be decoded into days and seconds (t.days, t.seconds), not hours!  
* overcome this issue by t.seconds / 60 / 60

### Day 2:
