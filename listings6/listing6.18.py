# A function with annotations
def show(txt:"Text"="show() function")->"There is no result":
    print(txt)
# Calling the function
show()
# Dictionary of annotations
print(show.__annotations__)
# Annotations
for k in show.__annotations__:
    print(k,"-", show.__annotations__[k])