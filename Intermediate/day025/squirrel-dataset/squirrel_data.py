import pandas as pd

df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(df)
print(df.describe())
print(df.head())

fur_color=df["Primary Fur Color"]
# print(fur_color)

grey_squirrels_count=len(df[df["Primary Fur Color"]=="Gray"])
print(grey_squirrels_count)



cinnamon_squirrels_count=len(df[df["Primary Fur Color"]=="Cinnamon"])
print(cinnamon_squirrels_count)



black_squirrels_count=len(df[df["Primary Fur Color"]=="Black"])
print(black_squirrels_count)

data_dict={
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

color_dataframe=pd.DataFrame(data_dict)
color_dataframe.to_csv("squirrel_count.csv")
