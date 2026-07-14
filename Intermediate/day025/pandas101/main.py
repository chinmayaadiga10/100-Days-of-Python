# #the need for pandas and introduction to pandas -> 

import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

print(type(data)) #-> returns the type as a pandas data frame

# # 2 most important data types in pandas -> 1. dataframe 2. series

# #converting a dataframe to a dictionary -> 

data_dict=data.to_dict()
print(data_dict)

# #converting a series to a list ->
temp_list=data["temp"].to_list()
print(temp_list)

# #calculating average of list -> 
sum=0
for temp in temp_list:
    sum+=temp
print(sum/len(temp_list))

# #using inbuilt methods ->
avg = sum(temp_list)/len(temp_list)
print(avg)

# #calculating mean of temperatures using inbuilt pandas method -> 
print(data["temp"].mean())

# #calculating max value using pandas -> 
print(data["temp"].max())


# #Getting data in columns -> 
data["temp"] #syntax -> dataframe["column"]

print(data["condition"])
print(data.condition) #different implementation of same logic
    
    
# #Getting data present in rows of dataframe -> 
print(data[data.day=="Monday"])

# #printing row of data which has the highest temperature
highest_temp=data.temp.max()
print(data[data.temp==highest_temp])
print(data[data.temp==data.temp.max()])


monday=data[data.day=="Monday"]
print(monday)
print(monday.condition)

#Getting temperature of monday and converting it to fahrenheit -> 
temp=(monday.temp*(9/5))+32
print(temp)

#Creating a dataframe from scratch -> 

data_dict={
    "students":["ajay","janardhan","ghanshyam"],
    "scores":[94,78,89]
}

#creating dataframe
data=pandas.DataFrame(data_dict)
print(data)

#creating and storing values in a new csv file -> 
data.to_csv("new_data.csv")