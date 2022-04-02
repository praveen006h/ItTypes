from tkinter import *
from keyboard import write
import win32clipboard
import time


def copy():
    data = '' if TextArea.get("1.0", 'end')[0:-1] == '' else TextArea.selection_get()
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardData(13, data)
    win32clipboard.CloseClipboard()


def copy_all():
    data = TextArea.get("1.0", 'end')[0:-1]
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardData(13, data)
    win32clipboard.CloseClipboard()
    TextArea.tag_add('sel', "1.0", 'end')


def paste():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    TextArea.insert('end', data)


def showContext(event):
    x, y = event.x_root, event.y_root
    ContextMenu = Menu(win, tearoff=0)
    ContextMenu.add_command(label="Copy  ", command=copy)
    ContextMenu.add_command(label="Copy All ", command=copy_all)
    ContextMenu.add_separator()
    ContextMenu.add_command(label="Paste", command=paste)

    ContextMenu.tk_popup(x,y)


def proceed():
    text1 = TextArea.get("1.0",'end')[0:-1]
    time.sleep(5)
    write(text1)


win = Tk()
win.title("It Types")
win.geometry("700x550")
win.resizable(0,0)
win.configure(bg="#505166")
lHead = Label(win,text="Paste Your Text Here :",font="Helvetica 15 ", bg="#505166", fg="#ffffff")
lHead.place(x=70,y=10)
lMessage = Label(win, text="Place your cursor where u want to type, soon after clicking 'Proceed!'", font="Helvetica 15 ", bg="#505166", fg="#ffffff")
lMessage.place(x=30, y=460)
TextArea = Text(win, height=25, width=70)
TextArea.place(x=50,y=50)
TextArea.configure(bg="#eeeeee")
TextArea.bind("<Button-3>", showContext)

bSub = Button(win, text="Proceed!", command=proceed, width=20, font="Helvetica 12 ",)
bSub.place(x=220, y=500)
mainloop()
