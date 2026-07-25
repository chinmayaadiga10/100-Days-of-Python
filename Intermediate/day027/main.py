# comes pre installed with python - no need to install from pypi.org
# generally, instead of using import , we use from  import *

from tkinter import *

window = Tk()

# giving title to the  window
window.title("My first GUI Program")

# this is the default size of the window; unless the user resizes the window or there are so many buttons or components that the window ends up resizing
window.minsize(width=500, height=300)

# adding padding to the main window
window.config(padx=20, pady=20)


# label ->

my_label = Label(text="I am a label", font=("Times New Roman", 24, "bold"))
my_label.pack()
# .pack places the component automatically on the center of the screen
my_label.pack(expand=True)
my_label.pack(side="")

my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)


my_label["text"] = "New Text"
my_label.config(text="new text")


# Creating buttons using  tkinter module ->


def button_clicked():
    print("I got clicked")
    new_input = input.get()
    my_label.config(text=new_input)


button = Button(text="Click Me !", command=button_clicked)
# button.pack()

button.grid(column=1, row=1)


new_button = Button(text="newly created", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry component ->

input = Entry(width=10)
print(input.get())
# input.pack()

# Trying out the place method ->
# input.place(x=0,y=0) # this is the top left of the screen

input.grid(column=3, row=2)

# ensures that the window stays on the screen
# has to be at the very end of the program
window.mainloop()
