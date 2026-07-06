#greets the user to the project and introduces itself
print("Welcome to the tip calculator!")

#asks for the total bill amount and stores it in bill variable. Notice that since the bill is an integer, we use int before input
bill=int(input("What was the total bill Amount?\n$"))

tip=int(input("How much tip would you like to give in percentage? 10,12 or 15?"))
people=int(input("How many people to split the bill"))
total_bill=bill*tip/100+bill
split=total_bill/people


#round function with two decimal parameters used to give us the final amount of the bill
final_amount=round(split,2)

#the final amount is displayed using formatted strings
print(f"The total amount to be paid by each individual is : {final_amount}")