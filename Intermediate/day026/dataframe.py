import pandas as pd
student_dict={
    "student":["angela","james","lily"],
    "score":[88,78,69],
}

#Looping through dictionaries -> 

for (key,value) in student_dict.items():
    print(key,value)
    
    
# Creating a pandas dataframe -> 

student_dataframe=pd.DataFrame(student_dict)
print(student_dataframe)


# Looping through a dataframe ->

for(key,value) in student_dataframe.items():
    print(value)


# Loop through rows of data frame using inbuilt methods
for(index,row) in student_dataframe.iterrows():
    print(row)
    print(row.student) #each of the row is pandas series object so we can use dot notation to get a particular column value