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
CHECKMARK = "✔"
timer1 = None
# ---------------------------- TIMER RESET ------------------------------- #
def resetting_button():
    global reps
    windows.after_cancel(timer1)
    canvas.itemconfig(text_id,text = "00:00")
    label_1.config(text="TIMER")
    reps = 0
    label_2.config(text="")




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mechanism():
    global reps
    reps += 1
    work_min_timer = WORK_MIN
    short_break_timer = SHORT_BREAK_MIN
    long_break_timer = LONG_BREAK_MIN

    if reps%2 == 0:
        label_2.config(text=CHECKMARK * int(reps / 2))
        if reps != 8:
            counting_number(short_break_timer*60)
            label_1.config(text="BREAK",fg=PINK)
        else:
            counting_number(long_break_timer*60)
            label_1.config(text="BREAK",fg=PINK)
    else:
        counting_number(work_min_timer*60)
        label_1.config(text = "TIMER",fg=RED)

    if reps == 9:
        return

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counting_number(count:int):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec%60 < 10:
        count_sec =f"0{count_sec}"
    canvas.itemconfig(text_id,text =f"{count_min}:{count_sec}")
    global timer1
    if count > 0:
        timer1 = windows.after(1000,counting_number,count-1)
    else:
        timer_mechanism()

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("The pandomaro tech")
windows.config(padx=100,pady=100,bg=YELLOW)


# TIMER label
label_1 = Label(fg=RED,text="TIMER",width=10,font=("Times_New_Roman",25),background=YELLOW)
label_1.grid(column = 1,row = 0)

# Tomato image and the time
photo = PhotoImage(file="tomato.png")
canvas = Canvas(width="400",height="400",bg=YELLOW,highlightthickness=0)
canvas.create_image(200,200,image = photo)
text_id = canvas.create_text(200,200,text = "00:00",font=("Arial",30),fill= "white")
canvas.grid(column = 1, row = 1)


# Start Button
button_1 = Button(text="Start",command=timer_mechanism)
button_1.grid(column = 0,row = 2)

# Reset Button
button_2 = Button(text="Reset",command=resetting_button)
button_2.grid(column = 2,row = 2)

# Check mark
label_2 = Label(fg=GREEN,font=("Arial",20))
label_2.grid(column = 1,row =3)

windows.mainloop()
