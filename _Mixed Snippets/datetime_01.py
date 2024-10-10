# Date & Format
import datetime


print("\nDatetime Options:\n")

for each in dir(datetime.datetime):
	if not each.startswith("_"):
		print(each)



print("\n----------\n")

x = datetime.datetime.now()

print("Time is", x.time())
print("It is a", x.strftime("%A \n"))


y = datetime.datetime(1964, 5, 15) # Add a date in the past.

print(y)
print(y.strftime("It was a %A on the %dth of %B %Y"))

delta = x - y
print(f"\nDistance between these dates is {'{:,}'.format(delta.days)} days.")

print("\nMore Date Format Codes:  \nhttps://www.w3schools.com/python/gloss_python_date_format_codes.asp\n")

print("\n----------\n")

# Time Zones:

import pytz

print("All Time Zones:\n")

print(pytz.all_timezones)

#for each in pytz.all_timezones[:10]: # Remove [] for all.
#	print(each)

# See a particular timezone difference:
# Must use a specific location from all_timezones output:
location = 'Asia/Gaza'
tz = datetime.datetime(2024, 9, 25, 15, 30, 0, 0, tzinfo=pytz.timezone(location))

print(f"\nExample: \nThe time difference between \nhere and {location} is {str(tz).split('+')[1]}" )


input()