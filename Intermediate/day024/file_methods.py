#Reading from file , by default mode is set to read
with open("new_file.txt") as file:
    contents=file.read()
    print(contents)
    
#Writing to file -> 

#Using write mode will erase all the present contents of the file and replace with the text we pass using write method

with open("new_file.txt",mode="w")as file:
    file.write("Text Contents")

#Using append method to add new lines while retaining previous ones -> 

with open("new_file.txt",mode="a") as file:
    file.write("\nAdding new information from python")