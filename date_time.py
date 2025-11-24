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



#------------------------- Format datetime ----------------------

#In different places date and time represents differently , for ex., d/m/y in UK and m/d/y in US.
#strftime and strptime methods are used to handle this.

#--------- strftime() ---------------

#strftime() method is avaialble under datetime,date and time classes.It returns formatted string from given datettime ,date or time object.
#It takes one or more format codes and returns formatted string based on it.

"""
%Y: Year (e.g., 2024)
%m: Month (01-12)
%d: Day of the month (01-31)
%H: Hour (00-23)
%M: Minute (00-59)
%S: Second (00-59)

"""

import datetime

now = datetime.datetime.now()
t1 = now.strftime("%H:%M:%S")
print(t1)   # 15:25:10

dt1 = now.strftime("%d:%m:%y,%H-%M-%S")
print(dt1)  # 24:09:24,15-25-10

dt2 = now.strftime("%d-%m-%y,%H:%M:%S")
print(dt2)  # 24-09-24,15:25:10

today = datetime.date.today()
dt3 = today.strftime("%d:%m:%y,%H-%M-%S")
print(dt3)  # 24:09:24,00-00-00

time = datetime.time(11,5,34)
print(time.strftime("%H:%M:%S"))  # 11:05:34

#---------- strptime() -----------------------

#strptime() method is used to return datetime object from the given string(represents date and time).

#It takes two arguments .
#one is given string and another one is format code equivalent to given string in first argument.

#%d, %B and %Y format codes are used for day, month(full name) and year respectively.

import datetime

date_string = "December 25, 2019"
d1 = datetime.datetime.strptime(date_string,"%B %d, %Y")
print(d1)  # 2019-12-25 00:00:00

dt_string1 = "21 February, 2018"
d2 = datetime.datetime.strptime(dt_string1,"%d %B, %Y")
print(d2)  # 2018-02-21 00:00:00

dt_string2 = "21/05/1987,10:08:45"
dt3 = datetime.datetime.strptime(dt_string2,"%d/%m/%Y,%H:%M:%S")
print(dt3)  # 1987-05-21 10:08:45

#------------------------ pytz modle --------------------

#When working on projects we can represent their timezone .
#Rather than trying to handle timezone we cna use third party module pytz.

#We can use timezone() method from pytz module.

import datetime
import pytz

now_time = datetime.datetime.now()
print(now_time)  # 2024-09-24 15:58:17.556119

tz = pytz.timezone("America/New_York")
print(tz)  # America/New_York

nw_tz = datetime.datetime.now(tz)
print(nw_tz)  # 2024-09-24 06:28:17.561291-04:00

tz1 = nw_tz.strftime("%d:%m:%y, %H:%M:%S")
print(tz1)  # 24:09:24, 06:28:17    