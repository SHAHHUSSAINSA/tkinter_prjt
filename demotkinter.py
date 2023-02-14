from tkinter import *
import tkinter as tk
from tkinter import messagebox
def check_data():

       messagebox.showinfo('Attribute1 data',attribute1.get())
       messagebox.showinfo('Attribute2 data',attribute2.get())



user = Tk()
user.title('Cyber Attack')
user.minsize(300,300)
user.maxsize(750,500)
user.configure(background='#808080')

text_label = Label(user,text='CYBER ATTACK DECTECTION',fg='black',bg='#808080')
text_label.pack()
text_label.config(font=('verdana',22))

attribute1_label = Label(user,text='Attribute 1',fg='black',bg='#808080')
attribute1_label.pack(pady=(20,5))
attribute1_label.config(font=('verdana',14))

attribute1 = Entry(user,width=50)
attribute1.pack(ipady=5,pady=(1,15))

attribute2_label = Label(user,text='Attribute 2',fg='black',bg='#808080')
attribute2_label.pack(pady=(20,5))
attribute2_label.config(font=('verdana',14))

attribute2 = Entry(user,width=50)
attribute2.pack(ipady=5,pady=(1,15))

submit_btn = Button(user,text='SUBMIT',bg='white',fg='black',width=20,height=2,command=check_data)
submit_btn.pack(pady=(10,20))
submit_btn.config(font=('verdana',10))



user.mainloop()