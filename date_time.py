"""
To work on date and time python provides datetime module.
datetime module contains various clsses to work on date and time.

datetime.datetime   : This class is used to handle both date and time.
datetime.date       : To handle date
datetime.time       : To handle time
datetime.timedelta  : To get duration between two different dates/times.

✅ Common interview questions and answers:
Q1. What is datetime in Python?
A: The datetime module in Python provides classes for manipulating dates and times. It allows you to create timestamps, format dates, 
calculate differences, and handle time zones.

Q2. What is the difference between datetime and timedelta?
A:

datetime represents a specific point in time (date + time).
timedelta represents a difference or duration between two dates or times (in days, seconds, microseconds, etc.).

"""
#------------- datetime class ------------------#

import datetime

now = datetime.datetime.now()

print(now)  # output (2025-03-23 10:26:02.411560)

## Represent date

d1_date = datetime.datetime(2025,3,23)

print(d1_date)  ## 2025-03-23 00:00:00

## Represent date and time

d2_date_time = datetime.datetime(2025,3,23,10,26,12,4115)
print(d2_date_time)  #2025-03-23 10:26:12.004115

#--------------- date class ----------------

date = datetime.date(2025,3,23)
print(date) #2025-03-23

# Print year,month,day specifically

print(date.year) #2025
print(date.month) #3
print(date.day)    #23

# To print today's date

today = datetime.datetime.today()
print(today)  #2025-03-23 11:12:34.085501

"""
We can use today() method from date class to get current date.
timestamp() from date class gives the date
"""

## Get date from timestamp

dt = datetime.date.fromtimestamp(5263872)
print(dt) #1970-03-03

import datetime
# difference between two dates

d1 = datetime.date(1982,7,21)
d2 = datetime.date(2025,3,23)

d3_diff = d2-d1

print(d3_diff)

#yesterday

from datetime import datetime, timedelta

yesterday = datetime.now() -timedelta(days=1)
yesterday = datetime.now() -timedelta(days=2)

print(yesterday)
print(yesterday)

now = datetime.now()
print(now)

now1 = datetime.now()
print(now1.strftime("%Y-%m-%d %H:%M:%S0"))

future_date = datetime.now() + timedelta(days=10)

print(future_date)

past_time = datetime.now() - timedelta(days=3)

print(past_time)

custom_delta = timedelta(days=2, hours=8, minutes=30)

print(custom_delta)

now2 = datetime.now().date()

print(now2)


#Q5. How to parse a string into a datetime object?
date_str = "2025-03-23 12:01:00"

dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

print(dt)