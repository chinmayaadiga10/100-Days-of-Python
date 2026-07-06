import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

        return sum(cards)


def compare_cards(u_score, c_score):
    if u_score == c_score:
        return "The game ends in a draw"
    elif u_score == 21:
        return "You win with a blackjack"
    elif c_score == 21:
        return "Computer wins with a blackjack"
    elif u_score > 21:
        return "You cross the limit! The computer wins"
    elif c_score > 21:
        return "The computer steps over! You win the game"
    elif u_score > c_score:
        return "You win the game"
    else:
        return "The computer wins the game"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    gameState = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not gameState:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User cards: {user_cards} ,Current score : {user_score}")
        print(f"Computer cards: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        gameState = True
    else:
        user_deal = input("Type 'y' to deal cards and 'n' to not deal cards")
        user_deal.lower()
        if user_deal == "y":
            user_cards.append(deal_card())
        else:
            gameState = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"User final hand : {user_cards}, final score : {user_score}")
    print(f"Computer final hand : {computer_cards}, computer score : {computer_score}")
    print(compare_cards(user_score, computer_score))


while (
    input("Do you want to play a game of blackjack. Type 'y' for yes and 'n' for no")
    == "y"
):
    play_game()
