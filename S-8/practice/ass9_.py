# Use the `datetime` module to print the current date, calculate the date 100 days from today, and determine the day of the week for a given date.
import datetime as dt
print(f"Current Date: {dt.datetime.now().date()}")
print(f"Date 100 days from today: {dt.datetime.now().date() + dt.timedelta(100)}")