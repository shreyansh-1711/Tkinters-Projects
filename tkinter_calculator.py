from tkinter import *
f2 = Tk()
f2.title("My calculator")

text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)


def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""



btn7=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="c",bg="powder blue", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="red", font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text=".",bg="powder blue", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="-By Shreyansh jain",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)



f2.mainloop()