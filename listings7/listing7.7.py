# Import class from module
from datetime import date
# Object for realization of date
myday=date(2024,11,14)
# Checking the result
print("The first date:", myday)
# Using fields of the object
print("Year:", myday.year)
print("Month:", myday.month)
print("Day:", myday.day)
# Determining the day of the week
print("The day of the week:", myday.weekday())
print("The day of the week:", myday.isoweekday())
# Creating a new object based on an existing one
newday=myday.replace(1985, day=15)
# Checking the result
print("The second date:", newday)
# Creating a new object
newday=date.fromisoformat("1998-08-12")
# Checking the result
print("The third date:", newday)
# Object for the current date
thisday=date.today()
# Checking the result
print("Today:", thisday)
# Date difference
delta=myday-thisday
# Checking the result
print("See you soon:", delta)
