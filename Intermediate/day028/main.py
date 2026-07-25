from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


# function similar to start_timer, triggered from reset button
def reset_timer():
    global reps  # accessing global variable and resetting the value to 0
    reps = 0
    title_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
    canvas.itemconfig(
        timer_text, text="00:00"
    )  # resetting text on top of tomato to 00:00
    window.after_cancel(timer)  # cancelling the timer using window.after_cancel
    check_mark.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36))


# ---------------------------- TIMER MECHANISM ------------------------------- #

# understanding pomodoro -> 25 - 5 - 25 - 5 - 25 - 5 - 25 - 20


# this function starts the timer, triggered when start timer button is clicked
# the main goal is to track reps, and pass the value of timer accordingly and call the count_down function
def start_timer():
    global reps  # accessing global reps variable which is set to 0
    reps += 1  # reps value increased by 1 as soon as function activated
    work_seconds = WORK_MIN * 60  # 1500 seconds
    short_break_seconds = SHORT_BREAK_MIN * 60  # 300 seconds
    long_break_seconds = LONG_BREAK_MIN * 60  # 1200 seconds

    if reps % 2 == 0:  # for reps=2,4,6 -> short break is activated
        if reps != 8:  # if reps multiple of 2 and not equal to 8 -> short break
            title_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50))
            count_down(short_break_seconds)
        else:  # if reps = 8, long break is activated, text changed accordingly
            title_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50))
            count_down(long_break_seconds)
    else:  # for reps =1,3,5,7 => work mode is activated and text is changed
        title_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# this is the main function of the code, it carries out the countdown and changes the text on top of tomato dynamically


def count_down(
    count,
):  # the count argument is passed from the start_timer function, in seconds like 300,1200,1500

    # accessing global reps variable
    global reps

    # calculating minutes by diving count by 60, quotient -> minutes
    count_min = math.floor(
        count / 60
    )  # math.floor considers only the integers, imported from math module
    count_seconds = count % 60  # the seconds are the remainder
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"  # this is done so that if seconds is 9, then displayed as 09
    canvas.itemconfig(
        timer_text, text=f"{count_min}:{count_seconds}"
    )  # changing the text on top of the tomato
    if count > 0:
        global timer  # accessing global variable
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  # setting up the tkinter window
window.title("Pomodoro")  # title for the app
window.config(
    padx=100, pady=50, bg=YELLOW
)  # adding padding on x and y directions and the bg color

title_label = Label(
    text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50)
)  # title text that displays "TIMER"
title_label.grid(column=1, row=0)

# start button used to start the button, start_timer function called when button is clicked
start_button = Button(
    text="Start",
    bg=YELLOW,
    highlightbackground=YELLOW,
    borderwidth=0,
    command=start_timer,
)
start_button.grid(column=0, row=2)

# creates check mark to be displayed after completion of a rep, initially set to none or 0
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36))
check_mark.grid(column=1, row=3)

# reset button used to reset timer, reset_timer function called when this button is pressed
reset_button = Button(
    text="Reset",
    bg=YELLOW,
    highlightbackground=YELLOW,
    borderwidth=0,
    command=reset_timer,
)
reset_button.grid(column=2, row=2)


# creating the canvas of dimensions of the tomato.png image, giving yellow bg
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# images are added to the background of the canvas using the photoImage class, filename is specified
tomato_image = PhotoImage(file="tomato.png")

# image is added to the center of the canvas
canvas.create_image(100, 112, image=tomato_image)

# timer text to display the time on top of tomato
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


# utilizing infinite loop built into tkinter, allows the screen to be displayed continuously
window.mainloop()
