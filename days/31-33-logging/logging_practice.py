#%%
import itertools

import time
import random

import logbook
import sys

app_log = logbook.Logger('App')

colors = itertools.cycle(['Red', 'Amber', 'Green', 'Amber'])
def main():                          
    while True:
        for color in colors:
            if color == 'Red':
                print(f'The light is {color}.')
                delay = random.randint(1,5)
                time.sleep(delay) 
                app_log.trace(f'Red delay was {delay}')
            elif color == 'Green':
                print(f'The light is {color}.')
                delay = random.randint(1,5)
                time.sleep(delay) 
                app_log.trace(f'Green delay was {delay}')
            else:
                print(f'The light is {color}.')
                time.sleep(2) 
                
            
def init_logging(filename: str = None):
    level = logbook.TRACE
    
    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )

    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    # init_logging('days/31-33-logging/lights.log')
    init_logging()
#%%    main()
