# Import class from module
from datetime import time
# Object of realization of a moment in time
mytime=time(13,35,20)
# Checking the result
print("Time:", mytime)
# Using fields of the object
print("Hours:", mytime.hour)
print("Minutes:", mytime.minute)
print("Seconds:", mytime.second)
# Creating a new object based on an existing one
newtime=mytime.replace(15, second=45)
# Checking the result
print("Time:", newtime)
# Creating a new object
mytime=time.fromisoformat("12:34:56")