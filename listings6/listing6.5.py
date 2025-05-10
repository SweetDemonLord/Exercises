# Functions
def shift(val):
    print("shift() function")
    print("The original value is: ", val)
    val=["A","B","C"]
    print("The new value is: ", val)
def change(val):
    print("change() function")
    print("The original value is: ", val)
    if type(val)==list:
        for k in range(len(val)):
            val[k]+=1
    else:
        val+=1
    print("The new value is: ", val)

num=100
L=[10,20,30]
print(f"Variable num={num}")
change(num)
print(f"Variable num={num}")
print(f"L list={L}")
shift(L)
print(f"L list={L}")
change(L)
print(f"L list={L}")