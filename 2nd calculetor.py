from tkinter import *


def espclick(number):
    global operator
    operator= operator+ str(number)
    input_.set(operator)

def espclr():
    global operator
    input_.set(operator)
    operator=""

def espceqal():
    global operator
    operator=str(eval(operator))
    input_.set(operator)
    operator=""


cal =Tk()
operator=""
cal.title("calculetor")


input_=StringVar()
textdisplay=Entry(cal,font=("arial black",15,"italic"),textvariable=input_,bd="1",bg="green", insertwidth=3,justify="right").grid(columnspan=4)
  

  
buttonclr=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="C",command=espclr)
buttonclr.grid(row=1,column=0)
buttoneqal=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="=",command=espceqal)
buttoneqal.grid(row=1,column=1)
button0=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="0",command=lambda:espclick(0))
button0.grid(row=1,column=2)
buttonadd=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="/" , command=lambda:espclick("/"))
buttonadd.grid(row=1,column=3)
###############################################################################################################
button7=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="7",command=lambda:espclick(7))
button7.grid(row=2,column=0)
button8=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="8",command=lambda:espclick(8))
button8.grid(row=2,column=1)
button9=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="9",command=lambda:espclick(9))
button9.grid(row=2,column=2)
buttonadd=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="+",command=lambda:espclick("+"))
buttonadd.grid(row=2,column=3)

###############################################################################################################
button4=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="4",command=lambda:espclick(4))
button4.grid(row=3,column=0)
button5=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="5",command=lambda:espclick(5))
button5.grid(row=3,column=1)
button6=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="6",command=lambda:espclick(6))
button6.grid(row=3,column=2)
buttonadd=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="*",command=lambda:espclick("*"))
buttonadd.grid(row=3,column=3)
###############################################################################################################
button1=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="1",command=lambda:espclick(1))
button1.grid(row=4,column=0)
button2=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="2",command=lambda:espclick(2))
button2.grid(row=4,column=1)
button3=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="3",command=lambda:espclick(3))
button3.grid(row=4,column=2)
buttonadd=Button(cal,padx=10,pady=10, fg="white",bg="black",font=("arial black",15,"italic"),text="-",command=lambda:espclick("-"))
buttonadd.grid(row=4,column=3)
###############################################################################################################









cal.mainloop()