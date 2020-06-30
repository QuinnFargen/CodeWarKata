
# years, days, hours, minutes and seconds.

min = 60;hour = 3600;day = 86400;year = 31536000

seconds = 315360004
years = round(seconds / year); seconds = seconds - (year * years)
days = round(seconds / day); seconds = seconds - (day * days)
hours = round(seconds / hour); seconds = seconds - (hour * hours)
mins = round(seconds / min); seconds = seconds - (min * mins)
secs = seconds

from math import floor

def str_duration(time, label):
    if time == 0:
        return ''
    if time == 1:
        return '1 ' + label
    else :
        return str(time) + ' ' + label + 's'

def str_final(TimeList):
    if len(TimeList) == 2:
        return TimeList[0] + ' and ' + TimeList[1]
    if len(TimeList) == 3:
        return TimeList[0] + ', ' + TimeList[1] + ' and ' + TimeList[2]
    if len(TimeList) == 4:
        return TimeList[0] + ', ' + TimeList[1] + ', ' + TimeList[2] + ' and ' + TimeList[3]
    if len(TimeList) == 5:
        return TimeList[0] + ', ' + TimeList[1] + ', ' + TimeList[2] + ', ' + TimeList[3] + ' and ' + TimeList[4]


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    min = 60;hour = 3600;day = 86400;year = 31536000
    years = floor(seconds / year); seconds = seconds - (year * years)
    days = floor(seconds / day); seconds = seconds - (day * days)
    hours = floor(seconds / hour); seconds = seconds - (hour * hours)
    mins = floor(seconds / min); seconds = seconds - (min * mins)
    secs = seconds
    year_str = str_duration(years,'year')
    day_str = str_duration(days,'day')
    hour_str = str_duration(hours,'hour')
    min_str = str_duration(mins,'minute')
    sec_str = str_duration(secs,'second')
    AllTimeList = [year_str,day_str,hour_str,min_str,sec_str]
    TimeList = [i for i in AllTimeList if i != '']
    if len(TimeList) == 1:
        return TimeList[0]
    return str_final(TimeList)




seconds = 3153600042
format_duration(seconds)








test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")