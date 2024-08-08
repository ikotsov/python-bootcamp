import random
from art import stages

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

lives = len(stages)

while lives > 0:
    letter_guessed = input("Guess a letter: ").lower()

    for index, letter in enumerate(word_letters_list):
        if letter == letter_guessed:
            display_letter_list[index] = letter

    display = separator.join(display_letter_list)
    print(display)

    if letter_guessed not in word:
        lives -= 1
        print(stages[lives])

    if lives == 0:
        print("You lose")
