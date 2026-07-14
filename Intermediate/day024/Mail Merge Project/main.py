PLACEHOLDER="[name]"

#this set of lines is to open the invited names file and add them to a list called names.

with open("./Input/Names/invited_names.txt","r")as names_file:
    names=names_file.readlines()
    print(names)

#we are opening the sample letter and reading the contents as saving in letter_contents    
with open ("./Input/Letters/starting_letter.txt")as letter_file:
    letter_contents=letter_file.read()
    
    #for loop to loop through the names list and each individual name is stripped.
    for name in names:
        stripped_name=name.strip()
        
        #the placeholder is replaced with stripped name and saved in new_letter variable
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)    
        
        #creating new letters with filename same as the stripped name, using write mode and writing the new_letter using write method. This way we created a new letter with name personalization
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w")as completed_letter:
            completed_letter.write(new_letter)