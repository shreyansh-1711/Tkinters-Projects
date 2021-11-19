from tkinter import *
root = Tk()
root.geometry("700x700")
Gender = StringVar()
check = StringVar()
var_name = StringVar()
var_password = StringVar()

def show():
    if(check.get()=="1"):
        result = f"Your name is : {var_name.get()}\n Your password is : {var_password.get()}"
        print(result)

lbl_heading = Label(root, text="USER ENTRY FORM", font="arial 20 italic", bg="black", fg="white", bd=3, relief=SUNKEN)
lbl_heading.pack(fill=X)

lbl_footer = Label(root, text="User Entry Form", font="arial 20 italic", bg="black", fg="white", bd=3, relief=SUNKEN)
lbl_footer.pack(side=BOTTOM)

lbl_name = Label(root, text="Enter Your Name: ", font="arial 20 italic", fg="white", bg="black")
lbl_name.place(x=10, y=120)
ert_name = Entry(root, font="arial 20 italic", textvariable=var_name)
ert_name.place(x=250, y=120)

lbl_pass = Label(root, text="Enter Your Password: ", font="arial 20 italic", fg="white", bg="black")
lbl_pass.place(x=10, y=200)
ert_password = Entry(root, font="arial 20 italic", show="$", textvariable=var_password)
ert_password.place(x=350, y=200)

lbl_gender = Label(root, text="Select Your gender", font="arial 20 italic", fg="white", bg="black")
lbl_gender.place(x=10, y=280)
rbtn_genderm = Radiobutton(root, text="Male", value="male", font="arial 20 italic", variable=Gender)
rbtn_genderm.place(x=300, y=280)

rbtn_genderf = Radiobutton(root, text="Female", value="female", font="arial 20 italic", variable=Gender)
rbtn_genderf.place(x=400, y=280)

Gender.set("Male")

chk_accept = Checkbutton(root, text="Accept ot Not?", font="arial 20 italic", onvalue=1, offvalue=0, variable=check)
chk_accept.place(x=20, y=360)

check.set(0)



root.mainloop()