import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def get_turns(users_chosen_difficulty):
    if users_chosen_difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(users_guess, answer):
    if users_guess == answer:
        print(f"You got it! The answer was {answer}")
        return True
    else:
        if users_guess < answer:
            print("Too low")
        else:
            print("Too high.")
        return False


def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(answer)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = get_turns(difficulty)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        answer_correct = check_answer(guess, answer)

        if answer_correct:
            break
        else:
            attempts -= 1

        if attempts == 0:
            print("You' ve run out of guesses, you lose")
        else:
            print("Guess again")


game()
