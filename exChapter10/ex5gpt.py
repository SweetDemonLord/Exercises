class AlphabetException(Exception):
    """
    Пользовательский класс исключения, который хранит список букв алфавита.
    """

    def __init__(self, alphabet_list):
        self.alphabet_list = alphabet_list

    def __str__(self):
        return f"Список букв алфавита в обратном порядке: {self.alphabet_list}"


def generate_reverse_alphabet(index=25, alphabet=None):
    """
    Рекурсивная функция, которая генерирует список букв алфавита в обратном порядке.
    """
    if alphabet is None:
        alphabet = []

    # Базовое условие для выхода из рекурсии
    if index < 0:
        # Генерируем исключение с результатом
        raise AlphabetException(alphabet)

    # Добавляем букву в список в обратном порядке
    alphabet.append(chr(ord('A') + index))

    # Рекурсивно вызываем функцию для следующей буквы
    return generate_reverse_alphabet(index - 1, alphabet)


def main():
    try:
        # Запускаем рекурсивную функцию для генерации букв
        generate_reverse_alphabet()
    except AlphabetException as e:
        # Обрабатываем исключение и выводим результат
        print(e)


if __name__ == "__main__":
    main()
