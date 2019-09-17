#%%
import time
from functools import wraps


#%%
def mydecorator(function):
    @wraps(function)
    def wrapper(*arg, **kwargs):
        result = function(*arg, **kwargs)
        return result
    return wrapper




#%%
@mydecorator
def my_function(args):
    pass

#! this is equivalent to:
# def my_function(args):
#     pass
# my_function = mydecorator(my_function)

#%%
def get_profile(name, active=True, *sports, **awards):
    print('Positional arguments (required): ', name)
    print('Keyword arguments (not required, default values): ', active)
    print('Arbitrary argument list (sports): ', sports)
    print('Arbitrary keyword argument dictionary (awards): ', awards)

#%%

def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    # return wrapper as a decorated function
    return wrapper


#%%
@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')

#%%
get_profile('bob', True, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')


#%%
def timeit(func):
    '''Decorator to time a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):

        #!before calling the decorated function
        print('== starting timer')
        start = time.time()

        #! call the decorated function
        func(*args, **kwargs)

        #! after calling the decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')

    return wrapper
#%%

def generate_report():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')

generate_report()
#%%
@timeit
def generate_report():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')


generate_report()


#%%
