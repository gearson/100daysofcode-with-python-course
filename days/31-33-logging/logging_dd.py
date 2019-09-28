import logbook
import sys
import time

level = logbook.TRACE
# log_filename = 'days/31-33-logging/test.log'
log_filename = ''

if not log_filename:
    logbook.StreamHandler(sys.stdout,
                          level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(log_filename,
                                     level=level).push_application()

app_log = logbook.Logger('App')

app_log.trace('log successful')
time.sleep(3)
app_log.warn('log successful')
app_log.notice('log successful')