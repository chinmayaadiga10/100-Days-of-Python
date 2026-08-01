import smtplib

my_email = "mygmail@gmail.com"
password = "app_password"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # tls stands for transport layer security - secures connection , encryption provided
connection.login(user=my_email, password=password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="mygmail@gmail.com",
    msg="Hello boss, i am glad this worked and it just unlocks an ocean of opportunities for me",
)

connection.sendmail(
    from_addr=my_email,
    to_addrs="mygmail@gmail.com",
    msg="Subject:Hello\n\nThis is the body part of the email",
)

connection.close()

# Better technique ->  connection.close() need not be used with this technique

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail()
