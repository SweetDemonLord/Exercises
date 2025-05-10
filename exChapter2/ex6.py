a,b,c=eval(input("Enter three numbers (separated by commas): "))
if a+b>c and a+c>b and b+c>a:
    print("A triangle with such sides can exist.")
else:
    print("A triangle with such sides can not exist.")