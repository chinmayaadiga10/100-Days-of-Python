# Understanding use of *args in python

# *args allows us to have any number of arguments in a function


# *args -> also known as unlimited positional arguments
def add(*args):
    sum = 0
    print(args[0])  # accessing specific index because args is a tuple
    print(args)
    print(type(args))  # the type of args is a tuple
    for n in args:
        sum += n
    print(sum)


add(2, 3, 4, 5, 6)
add(2, 3, 4)


# *kwargs ->


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)


def show_profile(**kwargs):
    print(f"Data type: {type(kwargs)}")
    print(f"Matrix Map: {kwargs}")


show_profile(name="Alice", age=30, city="Paris")


def make_profile(username, **kwargs):
    print(f"User: {username}")
    print(f"Extra Details: {kwargs}")


# Pass as many or as few details as you want
make_profile("coder123", status="active", theme="dark")
make_profile("gamerX", level=50)


def build_car(color, **kwargs):
    # .get(key, default_value) prevents errors if the key is missing
    wheels = kwargs.get("wheels", 4)
    sunroof = kwargs.get("sunroof", False)

    print(f"Car color: {color}")
    print(f"Number of wheels: {wheels}")
    print(f"Has sunroof: {sunroof}\n")


# Example A: Using defaults
build_car("Red")

# Example B: Overriding defaults
build_car("Black", wheels=6, sunroof=True)


def print_address(street, city, zip_code):
    print(f"Deliver to: {street}, {city} ({zip_code})")


# A standard dictionary
my_house = {"street": "123 Main St", "city": "Tech City", "zip_code": "94016"}

# The ** operator unpacks the dictionary keys as argument names
print_address(**my_house)
