import datetime as dt
import random
import smtplib

MY_EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
print(now)

day = now.day
print(day)

weekday = now.weekday()
print(weekday)

if weekday == 0:

    with open("quotes.txt", mode="r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        message = f"SUBJECT:Monday Motivation\n\n{quote}"
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
