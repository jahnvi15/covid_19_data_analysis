import tkinter as tk
from tkinter import *
import main
from main import f1
import tkinter.font as font
import time

    
def login_verify():
#get username and password
 
    username1 = vlogin.get()
    password1 = vpass.get()

 
    if username1=='admin':
            if password1=='root':
                Label(g,text=' Password verified',fg="hotpink", bg="steelblue",font= mf2,width = 30).grid(row=12,columnspan=9)

                
                print('Password verified ')
                print('Running COVID 19 Data Analysis ')
                g.destroy()
                f1()
                
            else:
                #print('password not recognised')
                label=Label(g,text=' password not recognised',fg="red", bg="steelblue",font= mf3)
                label.grid(row=12,columnspan=9)

                
 
    else:
            #print('user not found')
            Label(g,text=' user not found',fg="red", bg="steelblue",font= mf3,width = 30).grid(row=12,columnspan=9)

            
def login_verification():
    
    #print("working...")
    login_verify()


g=tk.Tk()
g.geometry('610x500')
g.configure(bg='mediumslateblue')
g.title('COVID 19')
#Label_middle.place

myfont = font.Font(family='Helvetica',size=10,weight='bold')
mf2=font.Font(family='Courier',size=20,weight='bold')
mf3=font.Font(family='Helvetica',size=15,weight='bold',underline=1)
mf4=font.Font(size=11)
mf5=font.Font(size=11 ,weight='bold')
#cyan
Label(g,text='Welcome To Covid 19 Data Analysis ',fg="hotpink", bg="navy",font= mf2,width=39).grid(row=0,columnspan=4)
Label(g,text='A Year in Global Pandemic',fg="hotpink", bg="ivory",font= mf2,width=39).grid(row=1,columnspan = 4)
'''
intro=Label(g,text=

,font=mf5,fg='ivory',bg='mediumorchid').grid (row=3,columnspan=4,rowspan=3,sticky=N+E+S+W)
'''

helu=Label(g, text="Enter Details below to Login",
           padx=10, pady=10,fg='ivory',bg='mediumslateblue',height=1,font=mf3).grid(row=6,columnspan=10)


Label(g, text='Username',height=0,font= mf2 ,fg='white',bg='mediumvioletred').grid(row=7 ,pady=29,ipadx=10)
Label(g, text='Password',height=0,font= mf2,fg='white',bg='mediumvioletred').grid(row=9,ipadx=10)


vlogin=StringVar()
vpass=StringVar()

log=tk.Entry(cursor='hand1',bg='darkslateblue',fg='hotpink',width=35,textvariable=vlogin,font=mf5).grid(row=7, column=2,ipady=6)
pas=tk.Entry(fg='ivory',bg='darkslateblue',cursor='hand1',width=35,textvariable=vpass,show='*',font=mf5).grid(row=9, column=2,ipady=6,pady=15)

b1 = Button(g, text='Login', cursor='hand2',bg='ivory', font= mf2, fg='darkorchid', width=25,command = login_verification ).grid(row=10,columnspan=8,pady=30)

g.mainloop()

