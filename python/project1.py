#For Project 1, I decided to go with example 3 "Write a script that tell you the time"
# I found inspiration and source code for this project from https://phoenixnap.com/kb/get-current-date-time-python

#importing datetime module as a constant for this code
import datetime

#code used to implement the time and then relay an output that will tell you the time
t = datetime.datetime.now()

print("The time is now: %s:%s:%s" % (t.hour, t.minute, t.second))