import math
import tkinter as tk

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
def reset_timer():
    # Pause the timer
    window.after_cancel(timer)  # type: ignore
    # Challenge
    """
    Set timer_text = "00:00", Change the title_label to "Timer",
    and Reset the checkmarks.
    """
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # Challenge
    """
    Use the reps variable to count down the appropriate number of seconds.
    When you run the program the timer needs to switch between counting down
    the work time and the break time (test with 1 minute rather than 25 minutes)
    """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if reps % 2 != 0:
    #     count_down(work_sec)
    # elif reps % 8 == 0:
    #     count_down(long_break_sec)
    # elif reps % 2 == 0:
    #     count_down(short_break_sec)

    # Challenge
    """
    During a long break, update the label to "Break" in red.
    Druing a short break, update the label to "Break" in pink.
    During work time, update the label to "Work" in green.
    """
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
## Wrong
# import time

# count = 5
# while True:
#     time.sleep(1)
#     count -= 1
## Solution
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0:
    #     count_sec = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Challenge
        """
        Add one checkmark for every two reps
        """
        marks = ""
        ## Wrong
        # if reps % 2 == 0:
        #     marks += "✔"
        #     check_marks_label.config(text=marks)
        ## Solution
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# * Canvas Widget
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_marks_label = tk.Label(fg=GREEN, bg=YELLOW)
check_marks_label.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
