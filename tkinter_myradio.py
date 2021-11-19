from tkinter import *
root = Tk()
gender = StringVar()
def show():
    print(gender.get())
lbl_gender = Label(root, text="select your gender -->", font="arial 20 italic")
lbl_gender.grid(row=0, column=0)

rdo_male = Radiobutton(root, text="Male", font="arial 20 italic", bg="black", fg="white", value="male", variable=gender)
rdo_male.grid(row=0, column=1)
rdo_female = Radiobutton(root, text="feMale", font="arial 20 italic", bg="black", fg="white", value="female",  variable=gender)
rdo_female.grid(row=0, column=2)

btn_b1 = Button(root, text="select", command=show)
btn_b1.grid(row=1, column=1)


root.mainloop()