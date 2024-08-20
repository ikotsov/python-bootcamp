import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(CARDS)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards = list(map(lambda x: x.replace(11, 1), cards))

    return sum(cards)


def determine_winner(user_score, computer_score):
    if user_score == computer_score:
        print("Draw")
        return

    if computer_score == 0:
        print("Lose, opponent has Blackjack")
        return

    if user_score == 0:
        print("Win with a Blackjack")
        return

    if user_score > 21:
        print("You went over. You lose.")
        return

    if computer_score > 21:
        print("Opponent went over You win.")
        return

    if user_score > computer_score:
        print("You win")
        return

    print("You lose")


def game():
    game_over = False

    computer_score = -1
    user_score = -1

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    while not game_over:
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")

        computer_score = calculate_score(computer_cards)
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's score: {computer_score}")

    determine_winner(user_score, computer_score)


game()
