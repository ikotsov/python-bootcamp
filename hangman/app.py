import random

word_list = ['aardvark', 'baboon', 'camel']

word = random.choice(word_list)
print(word)

letter_guessed = input("Guess a letter: \n").lower()

for letter in word:
    if letter == letter_guessed:
        print("Right")
    else:
        print("Wrong")
