def sum_integers(*args):
    """
    Функция для вычисления суммы целочисленных аргументов.
    Если аргумент не является целым числом, возникает исключение.
    """
    total = 0
    for arg in args:
        try:
            # Проверка, является ли аргумент целым числом
            if not isinstance(arg, int):
                raise ValueError(f"Аргумент '{arg}' не является целым числом.")
            total += arg
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue  # Пропускаем неверные значения и продолжаем вычисления
    return total

# Пример использования
try:
    result = sum_integers(1, 2, 3, "4", 5, 6, 7.5, 8)
    print(f"Сумма целых чисел: {result}")
except Exception as e:
    print(f"Произошла ошибка: {e}")