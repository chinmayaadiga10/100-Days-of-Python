import pandas



{"A": "Alfa", "B": "Bravo"}
df=pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(df)

new_dict={row.letter:row.code for (index,row) in df.iterrows()}
# print(new_dict)

user_name=input("Enter your name : ").upper()
    
# print(user_name)
name=[name for name in user_name]
# print(name)

nato_list=[]
for letter in name:
    nato_word=new_dict[f"{letter}"]
    nato_list.append(nato_word)
print(nato_list)
    

#using list comprehension -> 
output_list=[new_dict[letter] for letter in user_name]
print(output_list)
