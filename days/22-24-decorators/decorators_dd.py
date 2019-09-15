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
