def my_sum(n,*a, txt="Sum of numbers"):
    s=0
    for m in range(len(a)):
        s+=a[m]**n
    print(txt+":",s)
my_sum(1,100,200,300)
my_sum(2,10,20,30,txt="Sum of squares")