import math
from tkinter import *
from plyer import notification


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    mode_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_labal.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        mode_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        mode_label.config(text="BREAK", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        mode_label.config(text="WORK", fg=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = str(math.floor(count / 60))
    count_sec = str(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_min.zfill(2)}:{count_sec.zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,  count - 1)
    else:
        if reps % 2 == 0:
            check_labal.config(text="✓" * (reps // 2))
            notification.notify(title="休憩だよ", message="休憩を取りましょう。", app_name="Pomodoro Timer", app_icon="timer.ico")
        else:
            notification.notify(title="作業開始", message="作業を始めましょう。", app_name="Pomodoro Timer", app_icon="timer.ico")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

mode_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, foreground=GREEN)
mode_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=10, font=("Arial", 10, "normal"), borderwidth=0, bg=PINK, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=10, font=("Arial", 10, "normal"), borderwidth=0, bg=PINK, command=reset_timer)
reset_button.grid(column=2, row=2)

check_labal = Label(foreground=GREEN, font=(FONT_NAME, 20, "normal", ), bg=YELLOW, wraplength=120)
check_labal.grid(column=1, row=3)


window.mainloop()