print("Operations with a list of numbers...")
# Controlled code
try:
    nums=eval(input("Enter the list of numbers: "))
    print("Received the value: "+str(nums))
    a=int(nums[0])
    b=int(nums[3])
    print(str(a)+"/"+str(b)+"="+str(a/b))
# Exceptions handling
except ZeroDivisionError:
    print("ZeroDivisionError: attempting to divide by zero!")
except IndexError:
    print("IndexError: attempting to index out of range!")
except:
    print("Something went wrong!")
print("Completion of the program.")