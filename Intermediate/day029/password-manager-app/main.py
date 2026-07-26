from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

WHITE = "#fff"
BLACK = "#000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(4, 6))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    print("save data was clicked")
    website_name = website_input.get()
    username = username_input.get()
    password = password_input.get()
    print(website_name, username, password)
    details = True

    if len(username) == 0 or len(password) == 0 or len(website_name) == 0:
        messagebox.showinfo(title="oops", message="Please Don't leave any fields empty")
        details = False

    if details:

        # messagebox.showinfo(title="Title",message="Message")
        is_ok = messagebox.askokcancel(
            title=website_name,
            message=f"These are the details entered\nEmail: {username}\nPassword: {password}\nIs it okay to save ?",
        )

        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website_name} | {username} | {password}\n")
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)


canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

website_text = Label(
    text="Website :", fg=BLACK, bg=WHITE, highlightbackground=WHITE, borderwidth=0
)
website_text.grid(column=0, row=1)

website_input = Entry(width=35, fg=BLACK, bg=WHITE, highlightbackground=WHITE)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


username = Label(
    text="Email/Username :",
    fg=BLACK,
    bg=WHITE,
    highlightbackground=WHITE,
    borderwidth=0,
)
username.grid(column=0, row=2)

username_input = Entry(width=35, fg=BLACK, bg=WHITE, highlightbackground=WHITE)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "chinmay@gmail.com")


password = Label(
    text="Password :", fg=BLACK, bg=WHITE, highlightbackground=WHITE, borderwidth=0
)
password.grid(column=0, row=3)

password_input = Entry(width=20, fg=BLACK, bg=WHITE, highlightbackground=WHITE)
password_input.grid(column=1, row=3)

generate_button = Button(
    text="Generate Password",
    width=11,
    borderwidth=0,
    highlightbackground=WHITE,
    command=generate_password,
)
generate_button.grid(column=2, row=3)

add_password = Button(
    text="Add", width=33, borderwidth=0, highlightbackground=WHITE, command=save_data
)
add_password.grid(column=1, row=4, columnspan=2)


window.mainloop()
