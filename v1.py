from tkinter import *
from pyautogui import write

import time

def sub():
    text1 = TextArea.get("1.0",'end')[0:-1]
    print(text1)
    time.sleep(5)
    write(text1)


win = Tk()
win.geometry("900x700")
win.title("It Types")
win.configure(bg="#505166")
lHead = Label(win,text="Type Your Text Here :",font="Helvetica 15 ", bg="#505166", fg="#ffffff")
lHead.place(x=70,y=10)
TextArea = Text(win, height=35, width=100)
TextArea.place(x=50,y=50)
TextArea.configure(bg="#eeeeee")

bSub = Button(win, text="Proceed!", command=sub, width=20, font="Helvetica 12 ",)
bSub.place(x=350, y=650)
mainloop()
