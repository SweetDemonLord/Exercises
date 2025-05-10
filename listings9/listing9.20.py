# Creating an iterator
vals=iter([100,"A",[1,2]])
# Iterator override
try:
    print("The first:", next(vals))
    print("The second:", next(vals))
    print("The third:", next(vals))
    print("The fourth:", next(vals))
except StopIteration:
    print("There are no more values")