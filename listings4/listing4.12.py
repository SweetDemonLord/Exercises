# List with key values
days=["Mo","Tu","We","Th","Fr","Sa","Su"]
# Creating dictionaries
week={days[s]: s for s in range(len(days))}
myweek={d: days.index(d) for d in days}
# Checking results
print(week)
print(myweek)
# Creating another dictionary
sqrs={k: k**2 for k in range(1,11) if k%2!=0}
# Checking the result
print(sqrs)