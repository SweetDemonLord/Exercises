def generate_months():
     months = ["January", "February", "March", "April","May", "June",
               "July", "August", "September", "October", "November","December"]
     for month in months:
         yield month
for month in generate_months():
    print(month)