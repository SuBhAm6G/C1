# Write a function that creates a log file named `activity.log` and writes log messages with timestamps.
import datetime as dt
import time
def log_reg(message,filename='activity.log'):
    with open(filename, 'a') as f:
        f.write(message+': '+str(dt.datetime.now().strftime("%H:%M:%S"))+'\n')
log_reg("This is a log message")
time.sleep(2)
log_reg("This is another log message")
time.sleep(5)
log_reg("This is a third log message")