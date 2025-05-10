import math


def solve_equation(A):
    """
    Функция для решения уравнения A(A - 1) * x = sin(A).
    Если A = 0, x = -1, если A = 1, решение невозможно (деление на ноль).
    """
    if A == 0:
        return -1
    elif A == 1:
        return "Ошибка: решение невозможно, деление на ноль (A = 1)."
    else:
        try:
            # Вычисляем x из уравнения A(A - 1) * x = sin(A)
            x = math.sin(A) / (A * (A - 1))
            return x
        except ZeroDivisionError:
            return "Ошибка: деление на ноль."


def get_float_input(prompt):
    """
    Функция для получения числового ввода от пользователя с обработкой исключений.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, введите корректное число.")


# Основная часть программы
def main():
    print("Решение уравнения вида A(A - 1) * x = sin(A).")

    # Ввод значения A
    A = get_float_input("Введите значение A: ")

    # Решение уравнения
    result = solve_equation(A)

    print(f"Решение уравнения: x = {result}")


if __name__ == "__main__":
    main()