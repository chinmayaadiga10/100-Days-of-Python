bmi = 84 / 1.65 ** 2
print(bmi)#30.85399
int(bmi)#30
print(int(bmi ))#prints 30 as bmi ignoring decimal and digits after the decimal

print(round(bmi)) 
#the round function rounds off the number so 
print(round(bmi,2))
#the round function with two parameters- the second parameter decides the number of decimals to include

score=0
#user scores a point
score+=1
print(score)

print("Your score is "+str(score))
height=1.8
winning=True


#this technique is called as f-strings where format strings are used to insert variables instead of concatenation
print(f"Your score is ={score} and your height is {height}\nYou are winning is {winning}")