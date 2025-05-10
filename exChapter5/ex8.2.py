def encrypt(text):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    encrypted_text = []

    for char in text:
        if char.lower() in vowels:
            # Find the index of the vowel and get the next one
            index = vowels.index(char.lower())
            next_index = (index + 1) % len(vowels)  # Circular shift
            encrypted_char = vowels[next_index]

            # Preserve the original case
            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text.append(encrypted_char)

        elif char.lower() in consonants:
            # Find the index of the consonant and get the next one
            index = consonants.index(char.lower())
            if char.lower()!=consonants[len(consonants)-1]:
                next_index = (index + 1) % len(consonants)  # Circular shift
                encrypted_char = consonants[next_index]
            elif char.lower()==consonants[len(consonants)-1]:
                encrypted_char = vowels[0]
            # Preserve the original case
            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text.append(encrypted_char)

        else:
            # If not a letter, keep character unchanged
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def decrypt(text):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    decrypted_text = []

    for char in text:
        if char.lower() in vowels:
            # Find the index of the vowel and get the previous one
            index = vowels.index(char.lower())
            if char.lower()!=vowels[0]:
                prev_index = (index - 1) % len(vowels)  # Circular shift
                decrypted_char = vowels[prev_index]
            elif char.lower()==vowels[0]:
                decrypted_char = consonants[len(consonants)-1]
            # Preserve the original case
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text.append(decrypted_char)

        elif char.lower() in consonants:
            # Find the index of the consonant and get the previous one
            index = consonants.index(char.lower())
            prev_index = (index - 1) % len(consonants)  # Circular shift
            decrypted_char = consonants[prev_index]

            # Preserve the original case
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text.append(decrypted_char)

        else:
            # If not a letter, keep character unchanged
            decrypted_text.append(char)

    return ''.join(decrypted_text)


# Input text from the user
user_input = input("Enter text to encrypt: ")

# Encrypt the text
encrypted = encrypt(user_input)
print("Encrypted text:", encrypted)

# Decrypt the text
decrypted = decrypt(encrypted)
print("Decrypted text:", decrypted)
