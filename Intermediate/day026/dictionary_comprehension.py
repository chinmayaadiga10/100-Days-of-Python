#creates a new dictionary from the values in a list or in a dictionary

#new_dict={new_key:new_value for item in list}

import random

names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

student_scores={student:random.randint(1,100) for student in names}
print(student_scores)

#using conditional dictionary comprehension -> 

passed_students={student:score for (student,score) in student_scores.items() if score>=60}
print(passed_students)