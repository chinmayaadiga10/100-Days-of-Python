import random
from game_data import data
from art import logo
from art import vs

# random_celebrity=random.choice(data)
# print(random_celebrity)
# a_followers=random_celebrity["follower_count"]
# print(a_followers)
# print(f"{random_celebrity["name"]},{random_celebrity["description"]}, {random_celebrity["country"]}")


print(logo)
print("Welcome to the higher or lower game")
guess = True


while guess:

    def compare():
        score = 0
        a = random.choice(data)
        print(f"{a["name"]},{a["description"]}, {a["country"]}")
        aFollowers = a["follower_count"]
        data.remove(a)

        print(vs)

        b = random.choice(data)
        print(f"{b["name"]},{b["description"]}, {b["country"]}")
        bFollowers = b["follower_count"]
        data.remove(b)

        if aFollowers > bFollowers:
            higher = a

        else:
            higher = b

        choice = input("Who has more followers ? A or B")
        choice = choice.lower()
        if choice == higher:
            print("You have guessed correctly")
            score += 1

        else:
            print("Sorry that's wrong")
            print(f"Final score is : ")
            guess = False
