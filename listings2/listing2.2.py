# A number is entered
number=int(input("Enter a number: "))
# Upper bound for the divisor
num=number//2
# Initial value for the divisor
k=2
# Finding divisors of a number
while k<=num:
    # If a number is divisible by a number k
    if number%k==0:
        print("The number is not prime")
        # Completing the cycle operator
        break
    # If the condition is false
    else:
        # The value of the divisor increases
        k=k+1
# The block is executed if break statement is not executed
else:
    print("The number is prime")
# The message displays always
print("Verification completed")