#this function describes the length of the variables of any data type

name="Astronaut"
length=len(name)
print(length)

print(len(name))

name = "Angela"
length = len(name)
print(length)


#to use a length function for integers and floating values they must be converted to strings first and foremost
number=765
new_num=str(number)
print(len(new_num))

#using length function on float by converting it to string and then printing length subsequently
floater=354.3737
float1=str(floater)
print(len(float1))

#similar technique used to print the length of boolean values
bool=True
str_bool=str(bool)
print(len(str_bool))
