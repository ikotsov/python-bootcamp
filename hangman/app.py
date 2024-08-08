import random

separator = ''
placeholder_char = "_"

word_list = ['aardvark', 'baboon', 'camel']

word = random.choice(word_list)
word_letters_list = list(word)
print(word)

word_length = len(word)
display_letter_list = []

for position in range(word_length):
    display_letter_list.append(placeholder_char)

display = separator.join(display_letter_list)

print(display)

while display != word:
    letter_guessed = input("Guess a letter: ").lower()

    for index, letter in enumerate(word_letters_list):
        if letter == letter_guessed:
            display_letter_list[index] = letter

    display = separator.join(display_letter_list)
    print(display)
