import random
from data import celebrities
from art import vs


def get_random_celebrity():
    return random.sample(celebrities, 1)[0]


def format_data(celebrity):
    return f"{celebrity["name"]}, a {celebrity['description']}, from {celebrity['country']}"


def compare(answer, celebs):
    if answer == 'A':
        return celebs[0]['follower_count'] > celebs[1]['follower_count']
    elif answer == 'B':
        return celebs[1]['follower_count'] > celebs[0]['follower_count']
    return False  # In case of an invalid answer


def game():
    score = 0
    should_continue = True
    rand_celebrities = [get_random_celebrity(), get_random_celebrity()]

    while should_continue:

        print(f"Compare A: {format_data(rand_celebrities[0])}.")
        print(vs)
        print(f"Against B: {format_data(rand_celebrities[1])}.")

        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        result = compare(user_answer, rand_celebrities)

        if user_answer not in ['A', 'B']:
            print("Invalid input. You should type 'A' or 'B'. Restart the game.")
            should_continue = False

        if result:
            score += 1
            print(f"Your are right! Current score: {score}")
            rand_celebrities = [rand_celebrities[1], get_random_celebrity()]
        else:
            print(f"Sorry that's wrong. Final score {score}")
            should_continue = False


game()
