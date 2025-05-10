from datetime import datetime
years,months,days,hours,minute,seconds=eval(input("Enter year, month, day, "
                                                  "a number of hours,minutes,seconds the moment you need: "))
current_time=datetime.today()
moment_time=datetime(years,months,days,hours,minute,seconds)
interval=moment_time-current_time
print("The interval the current moment and the time specified by the user:",
      str(interval))