import art


# writing individual functions for all 4 operations :
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# adding all the operations into dictionary - key = symbol, value = function
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
state = True

num1 = float(input("Enter the first number :"))

while state:
    for symbols in operations:
        print(symbols)
    choice = input("Pick an operation :")
    num2 = float(input("Enter the second number :"))

    # using dictionary operations to perform calculations
    # print(operations["*"](4,8))
    answer = operations[choice](num1, num2)
    print(f"{num1} {choice} {num2}={answer}")

    interest = input("Enter 'y' to continue and 'n' to restart calculation")
    interest = interest.lower()
    if interest == "y":
        num1 = answer
    else:
        print("\n*20")
        state = False
