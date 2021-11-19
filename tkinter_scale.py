# from tkinter import *
# root = Tk()
# root.geometry("200x200")
# def show(x):
#     l1 = Label(root, text=x)
#     l1.place(x=40, y=40)
#
#
# s1 = Scale(root, orient=HORIZONTAL, sliderlength=25, showvalue=FALSE, command=show)
# s1.grid(row=1, column=1)
#
#
# root.mainloop()

from tkinter import *
from tkinter import Button, messagebox
root = Tk()
root.geometry("500x500")

def show1():
    messagebox.showinfo("title 1", message="This is show1")
def show2():
    messagebox.showwarning("title 1", message="This is show2")
def show3():
    messagebox.showerror("title 1", message="This is show3")

icon = PhotoImage(file=r"alexaa.png")
l1 = Label(root,image=icon)
l1.place(x=40, y=400)

f1 = Frame(root, bg="blue", bd=5, relief=SUNKEN)
f1.place(x=10, y=60, height=300, width=400)

b1 = Button(f1, text="b1", command=show1)
b1.place(x=10, y=20)

b2 = Button(root, text="b2", command=show2)
b2.place(x=110, y=20)

b3 = Button(f1, text="b3", command=show3)
b3.place(x=210, y=20)



root.mainloop()