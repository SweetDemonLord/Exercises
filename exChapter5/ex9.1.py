def remove_longest_and_shortest(text):
    words=text.split()
    if not words:
        return text
    shortest_word=min(words, key=len)
    longest_word=max(words, key=len)

    words.remove(shortest_word)
    words.remove(longest_word)
    return ' '.join(words)
user_input=input("Enter text: ")
new_text=remove_longest_and_shortest(user_input)
print("Result: ", new_text)