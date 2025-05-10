def get_integer_input(prompt):
    """
    Функция для получения целочисленного ввода от пользователя.
    Если ввод некорректен, вызывает исключение.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введено не целое число. Пожалуйста, попробуйте снова.")


def display_range(start, end):
    """
    Функция для отображения чисел в заданном диапазоне от start до end.
    """
    if start > end:
        print("Ошибка: начальное значение не может быть больше конечного.")
        return

    print(f"Целые числа в диапазоне от {start} до {end}:")
    for number in range(start, end + 1):
        print(number, end=" ")
    print()


# Основной блок программы
def main():
    print("Программа для отображения чисел в заданном диапазоне.")

    # Получаем два целых числа от пользователя
    start = get_integer_input("Введите начальное значение диапазона: ")
    end = get_integer_input("Введите конечное значение диапазона: ")

    # Выводим числа в заданном диапазоне
    display_range(start, end)


if __name__ == "__main__":
    main()