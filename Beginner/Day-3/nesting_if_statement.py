print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Please enter your age"))
    if age<=12:
        print("You have to pay $5")
        bill=5
    elif age<=18:
        print("You have to pay $7")
        bill=7
    else:
        print("You have to pay $12")
        bill=12
    photo=input("Do you want to have a photo taken?")
    if photo =="yes":
        bill+=3

    print(f"The final bill amount is : {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")



#the below is what i built for practice
print("Rollercoaster revision project")
print("Welcome to the rollercoaster!")
height=int(input("Please enter your height"))
bill=0
if height>=120:
    print("Congratulations! You can ride the rollercoaster!")
    age=int(input("Please enter your age"))
    if age<=12:
        print("You have to pay only 5$")
        bill=5
    elif age>=12 and age<=18:
        print("You have to pay 7$")
        bill=7
    else:
        print("You have to pay 12$")
        bill=12
    option=(input("Do you want to have a photograph taken?"))
    option=option.lower()
    if option=="yes":
        print("Wow! Your photograph will be taken")
        bill+=3
        print(f"The final bill amount is {bill}")
    else:
        print("No worries")
        print(f"The final bill amount is :{bill}")
else:
    print("Sorry you have to grow taller")