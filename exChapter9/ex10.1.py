class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

fib=FibonacciIterator(10)
for number in fib:
    print(number, end=' ')