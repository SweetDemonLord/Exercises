from datetime import datetime

# Function to get date
def get_date_input():
    while True:
        date_str=input("Enter a date in YYYY-MM-DD format: ")
        try:
            date=datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Not a valid date. Please try again.")
# Enter dates
print("Enter the first date.")
date1=get_date_input()
print("Enter the second date.")
date2=get_date_input()

# Determining a difference between two dates
delta = date2-date1
days_difference = delta.days
print(f"\nNUmber of full days between {date1} and {date2}: {abs(days_difference)} days")