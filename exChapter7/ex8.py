from datetime import datetime
hours,minute,seconds=eval(input("Enter Hours, Minutes and Seconds of the moment you need: "))

current_time=datetime.today()
moment_time=current_time.replace(hour=hours,minute=minute,second=seconds)
interval=moment_time-current_time
print("The interval the current moment and the time specified by the user:",
      str(interval))