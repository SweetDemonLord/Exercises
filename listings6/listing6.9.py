def sqr_sum(*n):
    s=0
    for a in n:
        s+=a*a
    return s
def get_sum(*n):
    s=0
    for a in n:
        if type(a)==int:
            s+=a
    return s
def get_text(*t):
    return " ".join(t)
print("Sum of squares:",sqr_sum(1,3,5))
print("Sum of squares:",sqr_sum(2,4,6,8,10))
print("Sum of numbers:",get_sum(2,"A",4,"B",6))
print("Sum of numbers:",get_sum(1,[2,3],4))
print("Sum of numbers:",get_sum())
print("Text:",get_text("Hi","everyone"))
print("Text:",get_text("A","B","C","D"))