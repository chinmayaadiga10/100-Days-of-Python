with open("file1.txt") as file1:
    numbers_1=file1.readlines()
    # print(numbers_1)

first_list=[int(x) for x in numbers_1]
print(first_list)

with open("file2.txt") as file2:
    numbers_2=file2.readlines()
    # print(numbers_2)

second_list=[int(x) for x in numbers_2]
print(second_list)

result=[x for x in first_list if x in second_list]
print(result)


# print(result)