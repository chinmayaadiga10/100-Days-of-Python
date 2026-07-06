import random

choice = input("Do you want to play a game of blackjack ? Type 'y' or 'n' : ")
choice.lower()

player_cards_chosen = []
player_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if choice == "y":
    from art import logo

    print(logo)

for i in range(2):
    random_element = random.choice(player_cards)
    player_cards_chosen.append(random_element)
# print(player_cards_chosen)
sum_player = 0
for num in player_cards_chosen:
    sum_player += num
# print(sum)

computer_card = random.choice(dealer_cards)
print(f"Your cards : {player_cards_chosen} , current score : {sum_player}")
print(f"Computer's first card : {computer_card}")

choice2 = input("Type 'y' to get another card, type 'n' to pass : ")

if choice2 == "y":
    card_chosen = random.choice(player_cards)
    player_cards_chosen.append(card_chosen)

    sum_player += card_chosen
    print(f"Your cards : {player_cards_chosen} , current score : {sum_player}")
    print(f"Computer's first card : {computer_card}")

choice3 = input("Type 'y' to get another card, type 'n' to pass : ")
