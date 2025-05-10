A="Number {}, text {} and text again {}"
txt=A.format(123,"Python",321)
print(txt)
txt="Number {0} - is {0: b} or {0: x}".format(42)
print(txt)
txt="Code: {0:05d}, symbol: {0:*^5c}".format(65)
print(txt)
txt="Number: {:_>+20.3E}".format(123.468)
print(txt)
B="{0:_{2}{1}s}"
num=6
for k in range(1, num+1):
    print(B.format("*",k,">"), end="")
    print(" "*(2*(num-k)), end="")
    print(B.format("*",k,"<"))