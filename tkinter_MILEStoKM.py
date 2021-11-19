from tkinter import *
root = Tk()
root.title("Miles to KM convertor")
root.minsize(width=300, height=100)
root.config(padx=20, pady=20)
root.geometry("300x300")


def calculate():
    miles = float(e1.get())
    miles_to_km = miles * 1.609344
    l3.config(text=f"{round(miles_to_km)}")






e1 = Entry(root,width=10,bg="black",fg="white")
e1.insert(END, string="0")
e1.grid(row=0, column=1)

l1 = Label(root, text="Miles", font="arial 16 italic")
l1.grid(row=0, column=2)

l2 = Label(root, text="is equal to", font="arial 16 italic")
l2.grid(row=1, column=0)

l3 = Label(root, text="0", font="arial 16 italic")
l3.grid(column=1, row=1)

l4 = Label(text="Km")
l4.grid(column=2, row=1)


button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)


root.mainloop()