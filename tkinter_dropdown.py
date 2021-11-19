# # from _typeshed import ReadOnlyBuffer
# from tkinter import ttk
# from tkinter import *


# root = Tk()
# def show():
#     x=language.get()
#     lbl_result = Label(root,text=x,font="arial 20")
#     lbl_result.place(x=10,y=250)
# root.geometry("500x500")
# language = ttk.Combobox(root,font="arial 20",value=("php","python","django"),state="readonly",justify="center")
# language.place(x=5,y=50,height=40,width=250)
# # language.current(1)
# language.set("select any subject")
# btn_b1 = Button(root,text="OK",command=show)
# btn_b1.place(x=50,y=150)
# root.mainloop()








from tkinter import *

root= Tk()
root.geometry("600x600")
def show():
    for i in range(1,11):
        lstbx_lb1.insert(i,"language "+str(i))
def select():
    x=lstbx_lb1.curselection()
    # x=x+1
    sum=""
    for i in x:
        # print(lstbx_lb1.get(i))
        sum = sum+lstbx_lb1.get(i)+"\n"

    lbl_result = Label(root,text=sum,font="arial 20")
    lbl_result.place(x=10,y=450)

def delete():
    lstbx_lb1.delete(lstbx_lb1.curselection())    


lstbx_lb1 = Listbox(root,selectmode=MULTIPLE)
lstbx_lb1.place(x=10,y=50)




btn_b1 = Button(root,text="OK",command=show)
btn_b1.place(x=20,y=350)

btn_select  = Button(root,text="select",command=select)
btn_select.place(x=60,y=350)

btn_del = Button(root,text="Delete",command=delete)
btn_del.place(x=20,y=550)




root.mainloop()