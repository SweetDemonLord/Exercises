from datetime import date
year,month,day1=eval(input("Enter year, month and day of the first date: "))
first_date=date(year,month,day1)
year,month,day2=eval(input("Enter year, month and day of the second date: "))
second_date=date(year,month,day2)
print(f"Number of full days between the first {first_date} "
      f"and second {second_date} date: "
      f"{second_date - first_date.replace(day=day1+2)}")