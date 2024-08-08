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
    print(f"************************** {lives} LIVES LEFT **************************")
    letter_guessed = input("Guess a letter: ").lower()

    if letter_guessed in display_letter_list:
        print(f"You 've already guessed {letter_guessed}")

    for index, letter in enumerate(word_letters_list):
        if letter == letter_guessed:
            display_letter_list[index] = letter

    display = separator.join(display_letter_list)
    print(display)
    if display == word:
        print("************************** YOU WIN **************************")
        break

    if letter_guessed not in word:
        lives -= 1
        print(f"You guessed {letter_guessed}, that's not in the word. You lose a life.")
        print(stages[lives])

    if lives == 0:
        print("************************** YOU LOSE **************************")
