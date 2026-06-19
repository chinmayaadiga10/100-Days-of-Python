import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&','*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
password=""

for char in range(0,num_of_letters):
    random_character = random.choice(letters)
    # print(random_character)
    password+=random_character

for symbol in range(0,num_of_symbols):
    random_symbol=random.choice(symbols)
    random_symbol=str(random_symbol)
    # print(random_symbol)
    password+=random_symbol

for num in range(0,num_of_numbers):
    random_number=random.choice(numbers)
    random_number=str(random_number)
    # print(random_number)
    password+=random_number
    

print(f"Your password is {password}")


#Hard Level
password_list=[]
for char in range(0,num_of_letters):
    random_number=random.choice(numbers)
    # random_number=str(random_number)
    password_list.append(random_number)

for symbol in range(1,num_of_symbols+1):
    random_symbol=random.choice(symbols)
    # random_symbol=str(random_symbol)
    password_list.append(random_symbol)

for char in range(1,num_of_numbers+1):
    random_letter = random.choice(letters)
    # random_letter=str(random_letter)
    password_list.append(random_letter)

print(password_list)
random.shuffle(password_list)
print(password_list)

secure_password=""
for char in password_list:
    secure_password=secure_password+char
print(f"The secure password that is generated is : {secure_password}")












