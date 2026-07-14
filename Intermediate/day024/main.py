#Technique 1 ->

file=open("my_file.txt") #open is inbuilt method in python, stored in variable called file
#behind the scenes, python has opened this file and is ready for next operation

contents=file.read()#read method -> returns contents of file as string
print(contents)


file.close()#to free up system resources


#Better Technique -> 

#Here, the file closes automatically and resource efficient, as file - file is name of variable
with open("my_file.txt") as file:
    contents=file.read()
    print(contents)
    