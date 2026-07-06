programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

empty_dictionary = dict()
empty_dictionary["add"] = "We are trying to add something new"
print(empty_dictionary)

# editing an item in the dictionary

programming_dictionary["Bug"] = "We are trying to change the value of the bug"
print(programming_dictionary)

# loop through a dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
