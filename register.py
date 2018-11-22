from tkinter import *
from tkinter import Tk, StringVar, ttk
import time 
import datetime

root=Tk()
root.title('register')
root.geometry('1350x650+0+0')
root.configure(background='lightblue')


#------------------------------ FRAME------------------------------------
leftmyframe=Frame(root, width= 1000, height=650,bd=8, relief='raise')
leftmyframe.pack(side=RIGHT)

rightmyframe=Frame(root, width= 350, height=630,bd=8, relief='raise')
leftmyframe.pack(side=LEFT)



leftmyframe1=Frame(leftmyframe, width= 1000, height=100,bd=8, relief='raise')
leftmyframe1.pack(side=TOP)
leftmyframe2=Frame(leftmyframe, width= 1000, height=550,bd=8, relief='raise')
leftmyframe2.pack(side=TOP)
leftmyframe1=Frame(rightmyframe, width= 350, height=215,bd=8, relief='raise')
leftmyframe1.pack(side=TOP)
leftmyframe2=Frame(rightmyframe, width= 350, height=415,bd=8, relief='raise')
leftmyframe2.pack(side=TOP)
#___________________________________ VARIABLE_______________________________
DateofOrder= StringVar()
value= StringVar()
value= StringVar()
value1= StringVar()
value2= StringVar()
value3=StringVar()
value4= StringVar()
value5= StringVar()
value6= StringVar()
value7= StringVar()
value8= StringVar()
value9= StringVar()
value10= StringVar()
value11= StringVar()
value12= StringVar()


#----___________________________________________COMPONENTS_____________________________________
DateofOrder.set(time.strftime('%d/%m/%y'))

#----___________________________________________LEFT FRAME _____________________________________
lblno=Label(leftmyframe1,font=('arial 10 bold'),text="NO.", bd=16)
lblno.grid(row=0, column=0, sticky=W)


lblStudentno=Label(leftmyframe1,font=('arial 10 bold'),text="STUDENT NO.", bd=16)
lblStudentno.grid(row=0, column=1, sticky=W)


lblstudentname=Label(leftmyframe1,font=('arial 10 bold'),text="STUDENT NAME", bd=16)
lblstudentname.grid(row=0, column=2, sticky=W)


lblCourse=Label(leftmyframe1,font=('arial 10 bold'),text="STUDENT COUSECODE", bd=16)
lblCourse.grid(row=0, column=3, sticky=W)





bt1=Button(leftmyframe1, text='fill', padx=2,pady=2, bd=2, fg="black",font=('arial',10, 'bold'),width=12, height=1).grid(row=0,column=5)
bt2=Button(leftmyframe1, text='fill', padx=2,pady=2, bd=2, fg="black",font=('arial',10, 'bold'),width=12, height=1).grid(row=0,column=6)
bt3=Button(leftmyframe1, text='fill', padx=2,pady=2, bd=2, fg="black",font=('arial',10, 'bold'),width=12, height=1).grid(row=0,column=7)


















root.mainloop()