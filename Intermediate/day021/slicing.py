#Understanding how list and tuple slicing works in python

piano_keys=["a","b","c","d","e","f","g"]

#1. basic slicing -> start index(inclusive), stop index(exclusive)
print(piano_keys[2:5])

#2.slicing from specific point to end of list, stop is empty
print(piano_keys[2:])


#3. slicing from beginning to specific point, stop value mentioned, start is empty
print(piano_keys[:6])

#4.using 3 arguments -> start, stop and step
print(piano_keys[2:6:2])

#5. just using the step argument to print every other element in the list
print(piano_keys[::2])

#6. reversing a list ->
print(piano_keys[::-1])


#all these methods are exactly same for tuples and can be used for similar results