#this is declaring and initializing a list with list items
states_of_america=["Delaware","Pennsylvania","Texas","Florida"]

#syntax to print a list is as follows:
print(states_of_america)#this prints the entire list

#the individual list items can be printed and their indexing starts form 0 to n-1 where n is the number of list elements

print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])
print(states_of_america[3])
# print(states_of_america[4])#this item does not exist in the list so it would give out an error - index error list out of range

#negative indexing lists:
print(states_of_america[-1])#prints the first item from the last that is Florida
print(states_of_america[-2])#prints the second item from the last that is Texas

# #lists are mutable data structures : these are data structures whose values can be altered 
states_of_america[1]="Pencilvania"
#here we are changing the second item from Pennysilvania to Pencilvania
print(states_of_america[1])
print(states_of_america)

#appending an item to the list: 

states_of_america.append("California")
print(states_of_america)

states_of_america.append("Angelaland")
print(states_of_america)

states_of_america.extend(["ChinmayaLand","Maximilian land"])

print(states_of_america)