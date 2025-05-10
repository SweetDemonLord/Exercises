def find_max_in_range(func, start, end):
    max_value = 0

    for x in range(start, end + 1):
        current_value = func(x)

        if max_value==0 or current_value > max_value:
            max_value = current_value

    return max_value


# Пример функции для тестирования:
def example_function(x):
    return x ** 2 - 4 * x + 5  # Например, квадратичная функция


# Пример использования:
start = 0
end = 10
result = find_max_in_range(example_function, start, end)
print(f"Наибольшее значение функции в диапазоне [{start}, {end}] равно {result}.")