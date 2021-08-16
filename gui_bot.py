#popcat Point(x=470, y=519)
from tkinter import *

import pyautogui as pg
import keyboard

def botclick(clicks=5):
    while True:
        pg.click(470,519,clicks=clicks)
        if keyboard.is_pressed('q'):
            break

app =Tk()
app.geometry("400x200")
app.iconbitmap('click.ico')
app.title('Bot Auto click')
label = Label(text="Bot Auto click ").pack()
button =Button(text='click me', command=botclick,width=30).pack(pady=10)
label = Label(text="กดปุ่ม Q เพื่อหยุดการทำงาน",width=30,fg="White",bg="Black").pack()

app.mainloop()
