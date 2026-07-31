height=float(input("Enter your height :"))
weight=int(input("Enter your weight : "))


if height > 200 :
    raise ValueError("please enter a valid value for height")

bmi=weight/height**2
print(bmi)