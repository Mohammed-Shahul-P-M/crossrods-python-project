import tkinter
from tkinter import  *

window = tkinter.Tk()
window.geometry('350x500')
window.resizable(0,0)
window.title('Calculator')

label = Label(window,text='0',anchor=SE,font=('Verdana',20))

label.pack(expand=True,fill='both')

btnrow1 = Frame(window ,bg='grey')
btnrow1.pack(expand=True,fill='both')

btnrow2 = Frame(window )
btnrow2.pack(expand=True,fill='both')

btnrow3 = Frame(window ,bg='grey')
btnrow3.pack(expand=True,fill='both')

btnrow4 = Frame(window)
btnrow4.pack(expand=True,fill='both')

# ------ first line of button goes here  -------

btn1 = Button(btnrow1,text='1',font=('Verdana',22),relief=GROOVE,border=0)
btn1.pack(side=LEFT,expand=True,fill='both')

btn2 = Button(btnrow1,text='2',font=('Verdana',22),relief=GROOVE,border=0)
btn2.pack(side=LEFT,expand=True,fill='both')

btn3 = Button(btnrow1,text='3',font=('Verdana',22),relief=GROOVE,border=0)
btn3.pack(side=LEFT,expand=True,fill='both')

btnplus = Button(btnrow1,text='+',font=('Verdana',22),relief=GROOVE,border=0)
btnplus.pack(side=LEFT,expand=True,fill='both')

#  -------  second line of buttons goes here --------

btn4 = Button(btnrow2,text='4',font=('Verdana',22),relief=GROOVE,border=0)
btn4.pack(side=LEFT,expand=True,fill='both')

btn5 = Button(btnrow2,text='5',font=('Verdana',22),relief=GROOVE,border=0)
btn5.pack(side=LEFT,expand=True,fill='both')

btn6 = Button(btnrow2,text='6',font=('Verdana',22),relief=GROOVE,border=0)
btn6.pack(side=LEFT,expand=True,fill='both')

btnminus = Button(btnrow2,text='-',font=('Verdana',22),relief=GROOVE,border=0)
btnminus.pack(side=LEFT,expand=True,fill='both')

#  ---------- third line of buttons goes here -------------

btn7 = Button(btnrow3,text='7',font=('Verdana',22),relief=GROOVE,border=0)
btn7.pack(side=LEFT,expand=True,fill='both')

btn8 = Button(btnrow3,text='8',font=('Verdana',22),relief=GROOVE,border=0)
btn8.pack(side=LEFT,expand=True,fill='both')

btn9 = Button(btnrow3,text='9',font=('Verdana',22),relief=GROOVE,border=0)
btn9.pack(side=LEFT,expand=True,fill='both')

btnmultiply = Button(btnrow3,text='x',font=('Verdana',22),relief=GROOVE,border=0)
btnmultiply.pack(side=LEFT,expand=True,fill='both')

# --------- fourth line of buttons goes here ----------

btndot = Button(btnrow4,text='.',font=('Verdana',22),relief=GROOVE,border=0)
btndot.pack(side=LEFT,expand=True,fill='both')

btn0 = Button(btnrow4,text='0',font=('Verdana',22),relief=GROOVE,border=0)
btn0.pack(side=LEFT,expand=True,fill='both')

btndivide = Button(btnrow4,text='/',font=('Verdana',22),relief=GROOVE,border=0)
btndivide.pack(side=LEFT,expand=True,fill='both')

btnequal = Button(btnrow4,text='=',font=('Verdana',22),relief=GROOVE,border=0)
btnequal.pack(side=LEFT,expand=True,fill='both')

window.mainloop()