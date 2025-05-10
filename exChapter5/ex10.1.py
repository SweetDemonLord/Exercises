def reverse_words(text):
    # Split the text into words using spaces as separators
    words=text.split()
    # Reverse the list of words
    reversed_words=words[::-1]
    # Join the reversed list back into a string
    return ' '.join(reversed_words)
# Input text from the user
user_input=input("Enter text: ")
# Create new text with words in reverse order
new_text=reverse_words(user_input)
# Output the result
print("Reversed words text:", new_text)