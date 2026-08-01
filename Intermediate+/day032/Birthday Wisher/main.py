import datetime as dt
import pandas as pd
import random
import smtplib

PLACEHOLDER="[NAME]"
MY_EMAIL="chinmayaadiga.sf@gmail.com"
PASSWORD="znjbggrejkayrwtg"

# reading birthday.csv file using pandas and storing data variable
data=pd.read_csv("./birthdays.csv")

# format -> {(12,24):(name,email,year,month,day)}    
birthday_dict={(data_row.month,data_row.day):tuple(data_row)  for (index,data_row) in data.iterrows()}   

now=dt.datetime.now()
month=now.month
day=now.day

today=(month,day)

if today in birthday_dict:
    print(birthday_dict[today])
    name=birthday_dict[today][0]
    to_email=birthday_dict[today][1]
    letter_number=random.randint(1,3)
    with open(f"./letter_templates/letter_{letter_number}.txt") as letter_template:
        letter_contents=letter_template.read()
        letter_contents=letter_contents.replace(PLACEHOLDER,name)
        
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        message=f"SUBJECT:HAPPY BIRTHDAY {name}\n\n{letter_contents}"
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=to_email,msg=message)
        
        
        