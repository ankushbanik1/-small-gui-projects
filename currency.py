from tkinter import *
root=Tk()
root.geometry("450x450+300+300")

heading= Label(root, text="wellcome", font=("arial",13,"bold"), fg="steelblue").pack()
entr_amt = Label(root, text="ENTER A AMOUNT TO CONVERT", font=("arial",15,"bold")).place(x=80, y=50)

my_num = IntVar()
ent_box = Entry(root, width= 50,bd=5, textvariable=my_num, bg= "yellow").place(x=80, y= 90)


def converter():
    here =my_num.get()
    final= here* 69.2
    lab1=Label(root, text=("Rs."+ str(final)), font=("arial 25 bold"), fg= "red").place(x=10, y=200)
def convert1():
    here =my_num.get()
    final= here* 102.8
    lab1=Label(root, text=("Rs."+ str(final)), font=("arialblack 25 bold"), fg= "red").place(x=10, y=300)

def reverse():
    here =my_num.get()
    final= here/ 69.2
    lab=Label(root, text=("$."+ str(final)), font=("arial 25 bold"), fg= "green").place(x=80, y=300)

button1= Button(root,text=" USA Concvert", width=12, height=2, bg= "red", command=converter).place(x=10 , y = 130)    

button1= Button(root,text="Reverse", width=12, height=2, bg= "lightgreen", command=reverse).place(x=150 , y = 130)    
button1= Button(root,text="  Uk convert  ", width=16, height=2, bg= "lightblue", command=convert1).place(x=300 , y = 130)    


































root.mainloop()