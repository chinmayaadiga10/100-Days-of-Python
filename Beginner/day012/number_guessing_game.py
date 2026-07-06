import random
from art import logo

print(logo)

chosen = random.randint(1, 100)
# print(chosen)


def easy():

    attempts = 10
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess == chosen:
            print("Congratulations!")
            print("You have successfully guessed the number")
            print(f"Your guess :{guess} and computer's choice : {chosen}")
            break
        elif guess < chosen:
            print("Your guess is too low.")
            attempts -= 1
        else:
            print("Your guess is too high")
            attempts -= 1

    if attempts == 0:
        print("You have exhausted your chances! Try again next time")


def hard():
    attempts = 5
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess == chosen:
            print("Congratulations!")
            print("You have successfully guessed the number")
            print(f"Your guess :{guess} and computer's choice : {chosen}")
            break
        elif guess < chosen:
            print("Your guess is too low.")
            attempts -= 1
        else:
            print("Your guess is too high")
            attempts -= 1

    if attempts == 0:
        print("Your chances are over! Try again next time")


print("Welcome to the number guessing game\n")
print("I am thinking of a number between 1 and 100")
level = input('Choose a difficulty. Type "easy" or "hard" :')
level = level.lower()
if level == "easy":
    easy()
else:
    hard()
