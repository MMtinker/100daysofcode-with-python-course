""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

import datetime

get_time_delta = input('Please enter the timer length in minutes: ')

time_now = datetime.datetime.now()
[print('\a') for x in range(1, 2)]

print('Current time: ' + str(time_now))

start_time = time_now
finish_time = start_time + datetime.timedelta(minutes=int(get_time_delta))

while finish_time > datetime.datetime.now():
    pass
else:
    [print('\a') for x in range(1, 10)]
    print('The time us UP!!!!! Current time is: ' + str(datetime.datetime.now()))

