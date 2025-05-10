from copy import deepcopy
winter_spring = {
    "June": 66,
    "July": 77,
    "August": 88,
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
}
summer_autumn = {
    "June": 6,
    "July":7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
months={}
for key in winter_spring:
    if key in summer_autumn:
        months[key]={winter_spring[key],summer_autumn[key]}
for key,value in months.items():
    print(f"{key} : {value}")