import datetime as dt

# gets current date and time
now = dt.datetime.now()
print(now)
year = now.year
print(year)

month = now.month
print(month)

day = now.day
print(day)

day_of_week = now.weekday()
print(day_of_week)


print(type(now))
print(type(year))

date_of_birth = dt.datetime(year=2006, month=2, day=27)
print(date_of_birth)
