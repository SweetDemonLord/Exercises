def display_characters(text, index=0):
    if index >= len(text):
        return
    print(text[index], end=" ")
    display_characters(text, index + 2)

# Пример использования функции
input_text = "Пример текста для проверки"
display_characters(input_text)