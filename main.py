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
def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    checkmark_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer_label.config(text="Working", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        reps = 0
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    timer_min = math.floor(count / 60)
    timer_sec = count % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"
    canvas.itemconfig(canvas_text, text=f"{timer_min}:{timer_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_label.config(text="✔")
        else:
            checkmark_label.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
img = PhotoImage(file="C:/Users/AssabTigle/PycharmProjects/Pomodoro App/tomato.png")
canvas.create_image(102, 112, image=img)
canvas_text = canvas.create_text(102, 130, fill="white", text="00:00", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

# Label
timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=3, column=1)

# Buttons
start_button = Button(text="Start", bg="pink", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="pink", font=(FONT_NAME, 10, "bold"), command=reset)
reset_button.grid(row=2, column=2)

window.mainloop()
