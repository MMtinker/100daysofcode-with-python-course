'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''

    find_time = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
    get_date = datetime.strptime(find_time.group(), '%Y-%m-%dT%H:%M:%S')

    # pass
    return get_date


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''

    first_event = None
    last_event = None
    for line in loglines:
        if 'Shutdown initiated' in line:
            if not first_event:
                first_event = line
            else:
                last_event = line

    get_first_event_time = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', first_event)
    first_event_time = datetime.strptime(get_first_event_time.group(), '%Y-%m-%dT%H:%M:%S')

    get_last_event_time = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', last_event)
    last_event_time = datetime.strptime(get_last_event_time.group(), '%Y-%m-%dT%H:%M:%S')

    time_delta = last_event_time - first_event_time
    # pass
    return time_delta

