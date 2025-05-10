import threading

# Функция для вычисления факториала числа
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Функция для вычисления двойного факториала числа
def double_factorial(n):
    result = 1
    # Для четных чисел, шаг 2, начиная с n, для нечетных — аналогично
    for i in range(n, 0, -2):
        result *= i
    return result

# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Класс для вычисления всех трех операций
class MathOperations:
    def __init__(self, number):
        self.number = number
        self.factorial_result = None
        self.double_factorial_result = None
        self.fibonacci_result = None
        self.lock = threading.Lock()  # Блокировка для синхронизации доступа к результатам

    # Функция для вычисления результатов в потоках
    def compute(self):
        # Создаем потоки для каждой операции
        thread1 = threading.Thread(target=self.compute_factorial)
        thread2 = threading.Thread(target=self.compute_double_factorial)
        thread3 = threading.Thread(target=self.compute_fibonacci)

        # Запускаем потоки
        thread1.start()
        thread2.start()
        thread3.start()

        # Ожидаем завершения всех потоков
        thread1.join()
        thread2.join()
        thread3.join()

        # Выводим результаты
        self.display_results()

    # Функция для вычисления факториала
    def compute_factorial(self):
        with self.lock:  # Блокировка для синхронизации
            self.factorial_result = factorial(self.number)

    # Функция для вычисления двойного факториала
    def compute_double_factorial(self):
        with self.lock:
            self.double_factorial_result = double_factorial(self.number)

    # Функция для вычисления числа Фибоначчи
    def compute_fibonacci(self):
        with self.lock:
            self.fibonacci_result = fibonacci(self.number)

    # Функция для вывода результатов
    def display_results(self):
        print(f"Факториал числа {self.number}: {self.factorial_result}")
        print(f"Двойной факториал числа {self.number}: {self.double_factorial_result}")
        print(f"Число Фибоначчи для {self.number}-го элемента: {self.fibonacci_result}")

# Главная функция
def main():
    number = int(input("Введите число для вычислений: "))
    math_operations = MathOperations(number)
    math_operations.compute()

if __name__ == "__main__":
    main()
