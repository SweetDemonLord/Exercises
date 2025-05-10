# Text variable
res="This is the number "
# Text is entered
txt=input("Enter the name of the number: ")
# Convert to lowercase
txt=txt.lower()
# Number identification
if txt=="one" or txt=="unit":
    res+="1"
elif txt=="two" or txt=="deuce":
    res+="2"
elif txt=="three" or txt=="troika":
    res+="3"
else:
    res+="is not identified"
# Result of identification
print(res)