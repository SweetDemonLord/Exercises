def solve_equation(A, B):
    """
    Функция для решения уравнения (A^2 - 1) * x = B
    Возвращает решение x или сообщение об ошибке.
    """
    try:
        # Вычисляем A^2 - 1
        coefficient = A ** 2 - 1

        # Проверяем случай, когда A = 1 или A = -1, и B = 0
        if coefficient == 0 and B == 0:
            return "Уравнение имеет бесконечно много решений. x - любое число."

        # Проверка, что коэффициент не равен нулю
        elif coefficient == 0:
            return "Ошибка: коэффициент (A^2 - 1) равен 0, и B ≠ 0, решение невозможно."

        # Находим x
        x = B / coefficient
        return x
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except Exception as e:
        return f"Произошла ошибка: {e}"


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
    print("Решение уравнения вида (A^2 - 1) * x = B.")

    # Ввод значений A и B
    A = get_float_input("Введите значение A: ")
    B = get_float_input("Введите значение B: ")

    # Решение уравнения
    result = solve_equation(A, B)

    print(f"Решение уравнения: {result}")


if __name__ == "__main__":
    main()