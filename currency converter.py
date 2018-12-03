from tkinter import*
root=Tk()
heading=Label(root, text='Convert Your Currency' ,font=('aria', 15 ,'bold') ,fg='green' ).pack()
ent_amt=Label(root,  text='Enter Your Amount', font=('aria', 20, 'bold'), fg='red').pack()



x=IntVar()
ent=Entry(root, textvariable=x ,width=200,bd=20,insertwidth=3, justify="right",bg='orange').pack()

def usconvert():
    here= x.get()
    final=here*70.02
    lab=Label(root,text=('here your Converted money:Rs.'+str(final)) ,font=('aria', 13,'bold') ,fg='green').place(x=10,y=270)
def usreverse():
    here= x.get()
    final=here/70.02
    lab=Label(root,text=('here your Converted money:$.'+str(final)) ,font=('aria',13,'bold'), fg='blue').place(x=10,y=290)
 
def ukconvert(): 
    here= x.get()
    final=here*103.02
    lab=Label(root,text=('here your Converted money in UK currency:'+str(final))  ,font=('aria', 13,'bold'), fg='green').place(x=10,y=330)

def ukreverse():
    here= x.get()
    final=here/103.02
    lab=Label(root,text=('here your Converted money:Rs.'+str(final)) ,font=('aria', 13,'bold') ,fg='red').place(x=10,y=320)



Button1=Button(root, text='USA dollar', font=('arial',15,'bold') ,fg='white',bg= "black", bd=1, command=usconvert).place(x=15, y=180)
Button2=Button(root, text='USA Reverse' ,font=('arial',15,'bold'),fg='black',bg= "yellow", bd=1, command=usreverse).place(x=140 ,y=180)
Button3=Button(root, text='UK Euro ' ,font=('arial',15,'bold') ,fg='black',bg= "lightblue", bd=1,command=ukconvert).place(x=270, y=180)
Button4=Button(root, text='UK Reverse  ', font=('arial',15,'bold'),fg='black',bg= "lightgreen", bd=1,command=ukreverse).place(x=370, y=180)






















root.geometry('500x500')
root.title('currency converter')
root.mainloop()
