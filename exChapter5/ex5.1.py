def merge_texts(text1, text2):
    # Получаем длины введенных текстов
    len1, len2 = len(text1), len(text2)
    result = []

    # Итерируемся по максимальной длине текстов
    for i in range(max(len1, len2)):
        if i < len1:
            result.append(text1[i])  # Добавляем букву из первого текста
        else:
            result.append('*')  # Если первый текст закончился, добавляем '*'

        if i < len2:
            result.append(text2[i])  # Добавляем букву из второго текста
        else:
            result.append('*')  # Если второй текст закончился, добавляем '*'

    return ''.join(result)  # Объединяем список символов в строку


# Ввод двух текстов от пользователя
text1 = input("Введите первый текст: ")
text2 = input("Введите второй текст: ")

# Создание нового текста
new_text = merge_texts(text1, text2)

# Вывод результата
print("Результат:", new_text)