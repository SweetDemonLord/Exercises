writers = {
    "Tolstoy": "War and peace",
    "Dostoevsky": "Crime and punishment",
    "Pushkin": "Eugen Onegin",
    "Checkov": "Thick and thin",
    "Gogol": "Dead souls"
}
correct=0
for s in writers.keys():
    print("Who wrote "+writers[s]+"? ")
    answer = input("Enter your answer: ")
    if answer == s:
        correct += 1
print("You have", correct, "correct answers.")
print("The answers of the test are presented below.")

for writer, book in writers.items():
    print(f"The writer: {writer} - Book: {book}")