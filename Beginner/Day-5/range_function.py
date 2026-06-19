#Range function

#the first argument inside the range operator talks about the start, the second talks about the stop and the 3rd argument talks about the step that is incremented by in each iteration

for number in range(1,11,3):
    print(number)

sum=0
for number in range(1,101): #start -> 1, stop->101, which means proceeds till 100
    sum+=number
print(sum)
