from tkinter import *

window = Tk()
window.title("Miles To Km Converter")
window.config(padx=15, pady=15)

window.minsize(width=600, height=300)


def calculate_miles():
    print("button working")
    miles = input.get()
    print(miles)
    miles = float(miles)
    km = miles * 1.60934
    km = int(km)
    label3.config(text=km)


label1 = Label(text="Miles", font=("Times New Roman", 30, "bold"))
label1.grid(column=2, row=0)
label1.config(padx=10)


input = Entry(width=20)
input.grid(column=1, row=0)

label2 = Label(text="is equal to", font=("Times New Roman", 30, "bold"))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Times New Roman", 30, "bold"))
label3.grid(column=1, row=1)
label3.config(padx=10, pady=10)

label4 = Label(text="Km", font=("Times New Roman", 30, "bold"))
label4.grid(column=2, row=1)

calculate = Button(text="Calculate", command=calculate_miles)
calculate.grid(column=1, row=2)


window.mainloop()
