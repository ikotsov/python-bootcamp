import random

placeholder_char = "_"

word_list = ['aardvark', 'baboon', 'camel']

word = random.choice(word_list)
print(word)

placeholder = ""
word_length = len(word)

for position in range(word_length):
    placeholder += placeholder_char

print(placeholder)

letter_guessed = input("Guess a letter: ").lower()

display = ""

for letter in word:
    if letter == letter_guessed:
        display += letter
    else:
        display += placeholder_char

print(display)
