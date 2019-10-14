#%%

def get_workout(day):
    if day == 'Monday':
        return 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        return 'Core'
    elif day == 'Thursday':
        return 'Legs'
    elif day == 'Friday':
        return 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        return 'Rest'
    raise ValueError('Not a day')

get_workout('Monday')
#%%
workouts = {
    'Monday': 'Chest+biceps',
    'Tuesday': 'Back+triceps',
    'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest',
}
workouts

#%%
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()

workouts2 = dict(zip(days, routines))
workouts2
#%%

def get_workout(day):
    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a day')
    return routine

#%%

i=0
for day in days:
    i += 1
    print(f'{i}. {day}')

#%%
# instead use:

for i, day in enumerate(days):
    print(f'{i}. {day}')


#%%
routines = 'Chest+biceps Back+triceps Core Legs Shoulders'.split()
timings = '45 45 30 55 45'.split()

workout_times = dict(zip(routines, timings))

max(workout_times.items(), key=lambda x: x[1])

#%%
max(workout_times.items())

#%%
