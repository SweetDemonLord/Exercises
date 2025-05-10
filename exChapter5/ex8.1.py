def encrypt(text):
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщ'

    encrypted_text = []

    for char in text:
        if char.lower() in vowels:
            # Находим индекс и заменяем на следующую гласную
            index = vowels.index(char.lower())
            next_index = (index + 1) % len(vowels)  # Циклический сдвиг
            encrypted_char = vowels[next_index]

            # Сохраняем регистр
            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text.append(encrypted_char)

        elif char.lower() in consonants:
            # Находим индекс и заменяем на следующую согласную
            index = consonants.index(char.lower())
            next_index = (index + 1) % len(consonants)  # Циклический сдвиг
            encrypted_char = consonants[next_index]

            # Сохраняем регистр
            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text.append(encrypted_char)

        else:
            # Если символ не буква, оставляем его без изменений
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def decrypt(text):
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщ'

    decrypted_text = []

    for char in text:
        if char.lower() in vowels:
            # Находим индекс и заменяем на предыдущую гласную
            index = vowels.index(char.lower())
            prev_index = (index - 1) % len(vowels)  # Циклический сдвиг
            decrypted_char = vowels[prev_index]

            # Сохраняем регистр
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text.append(decrypted_char)

        elif char.lower() in consonants:
            # Находим индекс и заменяем на предыдущую согласную
            index = consonants.index(char.lower())
            prev_index = (index - 1) % len(consonants)  # Циклический сдвиг
            decrypted_char = consonants[prev_index]

            # Сохраняем регистр
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text.append(decrypted_char)

        else:
            # Если символ не буква, оставляем его без изменений
            decrypted_text.append(char)

    return ''.join(decrypted_text)


# Ввод текста от пользователя
user_input = input("Введите текст для шифрования: ")

# Шифрование текста
encrypted = encrypt(user_input)
print("Зашифрованный текст:", encrypted)

# Дешифрование текста
decrypted = decrypt(encrypted)
print("Дешифрованный текст:", decrypted)