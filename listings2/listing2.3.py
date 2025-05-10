# A number is entered
number=int(input("Enter a number: "))
# The message about the first divisor of a number
print("Divisible by",1)
# Initial value for the divisor
k=1
# Finding divisors of a number
while k<=number//2:
    # The value of the divisor increases
    k=k+1
    # If a number is not divisible by a number k
    if number%k!=0:
        # Completing the current cycle
        continue
    # The message about a divisor of a number
    print("Divisible by",k)
        
# The message about the last divisor of a number
print("Divisible by",number)