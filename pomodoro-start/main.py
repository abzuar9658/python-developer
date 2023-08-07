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
REPS = 0
RESET = False
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global RESET

    RESET = True
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    global RESET

    print(RESET)
    if REPS > 8 or RESET:
        REPS = 0
        RESET = False
        return

    if not REPS == 0 and REPS % 8 == 0:
        print("LONG")
        title_label.config(text="Relax")
        count_down(LONG_BREAK_MIN * 60)
    elif not REPS % 2 == 0:
        title_label.config(text="Break")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="FOCUS")
        count_down(WORK_MIN * 60)
    REPS+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    work_mins = math.floor(count/60)
    work_secs = str(count % 60)
    work_secs = work_secs if len(work_secs) > 1 else '0' + work_secs

    canvas.itemconfig(timer_text, text=f"{work_mins}:{work_secs}")
    if(count > 0):
        window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,140, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="checked", bg=YELLOW)
check_marks.grid(column=1, row=3)
mainloop()