import random
import options

choose_from = [options.rock, options.paper, options.scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
user_choice = choose_from[user_input]

print(user_choice)

computer_choice = random.choice(choose_from)
print("Computer chose")
print(computer_choice)

user_wins = (user_choice == options.rock and computer_choice == options.scissors) or (
            user_choice == options.scissors and computer_choice == options.paper) or (
                        user_choice == options.paper and computer_choice == options.rock)

if user_wins:
    print("You win")
elif user_choice == computer_choice:
    print("It's a draw")
else:
    print("You lose")
