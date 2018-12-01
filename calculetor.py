from tkinter import *


def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_input.set(operator)

def btnClr(): 
    operator = ""
    text_input.set("")


def btneqal():
    global operator 
    operator = str(eval(operator))
    text_input.set(operator)
    operator = ""




cal= Tk()
operator=""
cal.title("calculator")

text_input=StringVar()
textdisplay=Entry(cal,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=3,bg="yellow",justify="right").grid(columnspan=4)

button7=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="7",command= lambda:btnClick(7))
button7.grid(row=1,column=0)
button8=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="8",command= lambda:btnClick(8))
button8.grid(row=1,column=1)
button9=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="9",command= lambda:btnClick(9))
button9.grid(row=1,column=2)
buttonadd=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="+",command= lambda:btnClick("+"))
buttonadd.grid(row=1,column=3)
button4=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="4",command= lambda:btnClick(4))
button4.grid(row=2,column=0)

button5=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="5",command= lambda:btnClick(5))
button5.grid(row=2,column=1)
button6=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="6",command= lambda:btnClick(6))
button6.grid(row=2,column=2)
buttonadd=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="-",command= lambda:btnClick("-"))
buttonadd.grid(row=2,column=3)
button1=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="1",command= lambda:btnClick(1))
button1.grid(row=3,column=0)
button2=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="2",command= lambda:btnClick(2))
button2.grid(row=3,column=1)
button3=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="3",command= lambda:btnClick(3))
button3.grid(row=3,column=2)
buttonadd=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="*",command= lambda:btnClick("*"))
buttonadd.grid(row=3,column=3)
button0=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="0",command= lambda:btnClick("0"))
button0.grid(row=4,column=0)
buttonclr=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="C",command= btnClr)
buttonclr.grid(row=4,column=1)
buttonequal=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="=",command= btneqal)
buttonequal.grid(row=4,column=2)
buttondiv=Button(cal, padx=16,pady=16,bd=8,fg="black",font=("arial",20, "bold"),text="/",command= lambda:btnClick("/"))
buttondiv.grid(row=4,column=3)






cal.mainloop()