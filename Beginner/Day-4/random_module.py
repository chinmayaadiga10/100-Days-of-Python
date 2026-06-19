import random
import my_module

# print(random_integer)
random_integer=random.randint(1,10)
#
print(my_module.my_favourite_number)

random_number_0_to_1=random.random()*10
print(random_number_0_to_1)

random_float=random.uniform(1,10)
print(random_float)


# Random heads or tails generator using random module
heads_tails=random.randint(1,2)
if heads_tails==1:
    print("Heads")
else:
    print("Tails")