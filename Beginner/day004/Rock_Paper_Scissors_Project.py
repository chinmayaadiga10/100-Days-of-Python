import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the rock paper and scissors game")
choice=int(input("What do you chose?Type 0 for Rock,Type 1 for paper and type 2 for scissors\n"))
print("Your choice is :")
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
else:
    print(scissors)

choice2=random.randint(0,2)
print("Computer chose :")
if choice2==0:
    print(rock)
elif choice2==1:
    print(paper)
else:
    print(scissors)

if choice==choice2:
    print("The game ends in a draw")
elif choice==0 and choice2==1:
    print("You lose the game")
elif choice==0 and choice2==2:
    print("You win the game!")
elif choice==1 and choice2==0:
    print("You win the game")
elif choice==1 and choice2==2:
    print("You lose the game")
elif choice==2 and choice2==0:
    print("You lose the game")
elif choice==2 and choice2==1:
    print("You win the game")





#modified rock paper scissors project using string inputs and string conditions:

#importing random module
import random 

# assigning rock, paper and scissor variables to the ASCII art which is our value
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#welcoming the user to the game
print("Welcome to the python rock paper scissors game!")

#asking the user to enter his choice in terms of either rock, paper or scissors
choice1=input("Please enter your choice. Type rock for rock , paper for paper and scissor for scissors\n")
choice1=choice1.lower()
print(f"You chose : {choice1}")
if choice1=="rock":
    print(rock)
elif choice1=="paper":
    print(paper)
else:
    print(scissors)

#list for computer to generate a random output from the following list
auto_list=["rock","paper","scissor"]
choice2=random.choice(auto_list)
print(f"The computer chose :{choice2}")
if choice2=="rock":
    print(rock)
elif choice2=="paper":
    print(paper)
else:
    print(scissors)

if choice1==choice2:
    print("The game ends in a draw")
elif choice1 =="rock" and choice2 == "paper":
    print("You lose!")
elif choice1=="rock" and choice2=="scissor":
    print("You win the game")
elif choice1=="paper" and choice2=="rock":
    print("You win the game")
elif choice1=="paper" and choice2=="scissor":
    print("You lose the game")
elif choice1=="scissor" and choice2=="rock":
    print("You lose")
elif choice1=="scissor" and choice2=="paper":
    print("You win the game")



