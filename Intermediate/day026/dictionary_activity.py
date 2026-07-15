# Activity 1 ->

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words=sentence.split() #.split() method is used to get list of individual words from a sentence
print(words)

result={word:len(word) for word in words}
print(result)


# Activity 2 -> 

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {temp:celsius*9/5+32 for(temp,celsius)in weather_c.items()}

print(weather_f)