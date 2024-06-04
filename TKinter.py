from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title("ERROR")
root.wm_attributes('-alpha', 0.7)
root.geometry("300x250")

root. resizable(width=False, height=False)

canvas = Canvas(root, width=300, height=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7 ,relheight=0.7)

title = Label(frame, text="ARE YOU GOMO?", bg='red', fg='white', font=40)
title.pack()
button = Button(frame, text="YES", bg='white', fg='yellow')
button.pack()

root.mainloop()