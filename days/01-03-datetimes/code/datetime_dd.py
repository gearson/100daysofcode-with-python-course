#%%
from datetime import datetime
from datetime import date
from datetime import timedelta
#%%
today = datetime.today()

#%%
type(today)

#%%
todaydate = date.today()

#%%
type(todaydate)

#%%
todaydate

#%%
todaydate.year

#%%
christmas = date(2019, 12, 24)
#%%
christmas - todaydate

#%%
(christmas - todaydate).days

#%%
if christmas is not todaydate:
    print('Sorry, there are still ' 
    + str((christmas - todaydate).days) 
    + ' days left until christmas')
else:
    print("It's Christmas")

#%%
t = timedelta(days = 4, hours = 10)

#%%
t.seconds  # seconds only go up to a max of 1 days!

#%%
t.seconds / 60 / 60

#%%
days_left = timedelta(days = 100)
today = datetime.today()

str(today + days_left)

#%%
