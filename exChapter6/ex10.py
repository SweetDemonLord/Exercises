def powers_of2(n):
    for i in range(1,n+1):
        print("2 to the power of", i, ":", end=" ")
        yield 2**i
N=int(input("Enter a number of numbers in the sequence of powers of 2: "))
for num in powers_of2(N):
    print(num)