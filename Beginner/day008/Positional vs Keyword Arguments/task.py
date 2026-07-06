# # Functions with input


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


#
#
greet_with_name("Jack Bauer")

# Functions with more than one parameter


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Chinmaya", "air force")

# keyword arguments example:
greet_with(location="California", name="Chinmaya")
