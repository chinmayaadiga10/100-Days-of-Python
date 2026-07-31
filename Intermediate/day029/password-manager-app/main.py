from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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
    new_data = {
        website_name: {
            "email": username,
            "password": password,
        }
    }

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
            try:
                with open("data.json", mode="r") as data_file:
                    #    json.dump(new_data,data_file,indent=4)

                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
                    print(data)

            finally:
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    username = username_input.get()
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            search_dict = json.load(data_file)
            print(search_dict)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        return
    else:

        try:
            password = search_dict[website]["password"]
            current_email = search_dict[website]["email"]
        except KeyError as error_message:
            messagebox.showinfo(
                title=website,
                message=f"The password for the website {website}  is not stored in the database",
            )
            print(f"Error is{error_message} ")

        else:
            print(password)
            password_input.delete(0, END)
            password_input.insert(0, password)
            messagebox.showinfo(
                title=website,
                message=f"Email : {current_email}\n Password : {password}",
            )


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

website_input = Entry(width=20, fg=BLACK, bg=WHITE, highlightbackground=WHITE)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(
    text="Search",
    width=11,
    borderwidth=0,
    highlightbackground=WHITE,
    command=find_password,
)
search_button.grid(column=2, row=1)


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
