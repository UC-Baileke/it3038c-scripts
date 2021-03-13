#For Project 1, I decided to go with example 3 "Write a script that tell you the time"
#For Project 2, I extended on project 1 so that it will also tell us how much hard drive space I have left
# I found inspiration and source code for this project #1 from https://phoenixnap.com/kb/get-current-date-time-python
# I found additional inspiration and source code for project 2 from https://stackoverflow.com/questions/48929553/get-hard-disk-size-in-python


#importing datetime module as a constant for this code
import datetime

#importing shutil module to use functions that allow info for disk usage
import shutil

#code used to let user know their outputs

print("Listed Below is your computers disk space and time.")

#code used to set an input/output for our disk space
total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

#code used to implement the time and then relay an output that will tell you the time
t = datetime.datetime.now()

print("The time is now: %s:%s:%s" % (t.hour, t.minute, t.second))