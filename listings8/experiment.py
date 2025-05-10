class MyClass:
    def __del__(self):
        print("An object is deleted")
A=MyClass()
print(A)

B=A
print(A)
print(B)
del A