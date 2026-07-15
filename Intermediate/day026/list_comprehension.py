#without using list comprehension -> 

# numbers=[1,2,3]
new_numbers=[]
for num in new_numbers:
    new_numbers.append(num+1)
print(new_numbers)

#doing the same task using list comprehension -> 

# [new_item for item in list]
numbers=[1,2,3,4]
new_numbers=[n+1 for n in numbers] #list comprehension used here
print(new_numbers)


#with strings -> 

name="idiosyncratic"
letters=[letter for letter in  name]
print(letters)

#trying with range -> 

range_numbers=range(1,10)
range_list=[num*2 for num in range_numbers]
print(range_list)

#conditional list comprehension -> 
#syntax -> new_list=[new_item for item in list if test]

names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_names=[name for name in names if len(name)<5]
print(short_names)

long_names=[name.upper() for name in names if len(name)>5]
print(long_names)