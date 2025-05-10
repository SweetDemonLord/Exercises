# Class
class MyClass:
    instances = {}

    def __init__(self, name, n=1):
        self.name = name
        self.code = None
        self.next = None
        self.set(n)
        MyClass.instances[name] = self
    def __del__(self):
        print("Deleting:", self.code)
        if self.next is not None:
            del self.next

    def set(self, n):
        if n == 1:
            self.next = None
        else:
            self.next = MyClass.instances.get(self.name) if self.name in MyClass.instances else MyClass(self.name, n - 1)
        self.set_code()

    def set_code(self, num=1):
        self.code = f"{self.name}[{num}]"
        print(self.code)
        if self.next:
            self.next.set_code(num + 1)

    def show(self):
        print(self.code)
        if self.next:
            self.next.show()

# Creating a chain of objects
print("One object:")
A = MyClass("Alpha")
print("Chain of objects:")
B = MyClass("Bravo", 5)
B.show()
print("Starting from the third object:")
if B.next and B.next.next:
    B.next.next.show()

# Deleting the objects
print("Deleting the objects:")
del A
del B


