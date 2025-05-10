# A number is entered
number=int(input("Enter a number: "))
# While the number is greater than 0
while number>0:
    # The last digit in a number
    digit=number%10
    # Displaying digits
    print("|"+str(digit), end="")
    # The last digit in the number is discarded
    number=number//10
# The last separator is displayed
print("|")

