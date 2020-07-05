import tkinter
from tkinter import *
from  tkinter import  messagebox

# ---------- calculator functions goes here -----------

value = ''
operator = ''
A = 0
dotbuttonStatus = False
def floatorintchecker(num):
    deference = num - int(num)
    if deference == 0 :
        return int(num)
    else:
        return num
def equalbtn_function():
    global A
    global operator
    global value
    global dotbuttonStatus
    value2 = value
    if operator == '+':
        secondvalue = float(value2.split('+')[1])
        result = A + secondvalue
        result = floatorintchecker(result)
        result = str(result)
        data.set(result)
        value = result
    elif operator == '-':
        secondvalue = float(value2.split('-')[1])
        result = A - secondvalue
        result = floatorintchecker(result)
        value = str(result)
        data.set(result)
    elif operator == '*':
        secondvalue = float(value2.split('x')[1])
        result = A*secondvalue
        result = floatorintchecker(result)
        value = str(result)
        data.set(result)
    elif operator == '/':
        secondvalue = float(value2.split('/')[1])
        if secondvalue == 0 :
            messagebox.showerror('Error : ','division by zero not defined')
            A = ''
            value = ''
            data.set('')
        else:
            result = A / secondvalue
            result = floatorintchecker(result)
            value = str(result)
            data.set(result)
    dotbuttonStatus = False
def btnclear_function():
    global value
    global A
    global operator
    value = ''
    operator = ''
    A = 0
    data.set(value)

def btnplus_function():
    global A
    global operator
    global value
    global  dotbuttonStatus
    A = float(value)
    operator = '+'
    value = value + '+'
    data.set(value)
    dotbuttonStatus = False

def btnminus_function():
    global A
    global operator
    global value
    global dotbuttonStatus
    A = float(value)
    operator = '-'
    value = value + '-'
    data.set(value)
    dotbuttonStatus = False

def btnmutiply_function():
    global A
    global operator
    global value
    global dotbuttonStatus
    A = float(value)
    operator = '*'
    value = value + 'x'
    data.set(value)
    dotbuttonStatus = False

def btndivide_function():
    global A
    global operator
    global value
    global  dotbuttonStatus
    A = float(value)
    operator = '/'
    value = value + '/'
    data.set(value)
    dotbuttonStatus = False

def btn1_function ():
    global  value
    value = value+'1'
    data.set(value)

def btn2_function():
    global  value
    value = value + '2'
    data.set(value)

def btn3_function():
    global  value
    value = value + '3'
    data.set(value)

def btn4_function():
    global  value
    value = value + '4'
    data.set(value)

def btn5_function():
    global  value
    value = value + '5'
    data.set(value)

def btn6_function():
    global  value
    value = value + '6'
    data.set(value)

def btn7_function():
    global  value
    value = value + '7'
    data.set(value)

def btn8_function():
    global  value
    value = value + '8'
    data.set(value)

def btn9_function():
    global  value
    value = value + '9'
    data.set(value)

def btn0_function():
    global  value
    value = value + '0'
    data.set(value)

def btndot_function():
    global dotbuttonStatus
    global value
    if dotbuttonStatus == False:

        value = value+'0.'
        dotbuttonStatus = True
        data.set(value)
    else:
        data.set(value)


window = tkinter.Tk()
window.geometry('350x500')
window.resizable(0,0)
window.title('Calculator')

data=StringVar()

label = Label(window,text='0',anchor=SE,font=('Verdana',20),bg='#d1c6a7',textvariable=data)
label.pack(expand=True,fill='both')

btnrow0 = Frame(window,)
btnrow0.pack(expand=True,fill='both')

btnrow1 = Frame(window ,bg='grey')
btnrow1.pack(expand=True,fill='both')

btnrow2 = Frame(window )
btnrow2.pack(expand=True,fill='both')

btnrow3 = Frame(window ,bg='grey')
btnrow3.pack(expand=True,fill='both')

btnrow4 = Frame(window)
btnrow4.pack(expand=True,fill='both')

# ------- optional buttons goes here --------

btnclear = Button(
    btnrow0,
    text='c',
    width='2',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btnclear_function)
btnclear.pack(side=LEFT,fill='y')

# ------ first line of button goes here  -------

btn1 = Button(btnrow1,text='1',font=('Verdana',22),
              relief=GROOVE,border=0,command=btn1_function)
btn1.pack(side=LEFT,expand=True,fill='both')

btn2 = Button(btnrow1,text='2',font=('Verdana',22),
              relief=GROOVE,border=0,command=btn2_function)
btn2.pack(side=LEFT,expand=True,fill='both')

btn3 = Button(btnrow1,text='3',font=('Verdana',22),
              relief=GROOVE,border=0,command=btn3_function)
btn3.pack(side=LEFT,expand=True,fill='both')

btnplus = Button(btnrow1,text='+',font=('Verdana',22),
                 relief=GROOVE,border=0,command=btnplus_function)
btnplus.pack(side=LEFT,expand=True,fill='both')

#  -------  second line of buttons goes here --------

btn4 = Button(btnrow2,text='4',font=('Verdana',22),
              relief=GROOVE,border=0,command=btn4_function)
btn4.pack(side=LEFT,expand=True,fill='both')

btn5 = Button(btnrow2,text='5',
              font=('Verdana',22),
              relief=GROOVE,border=0,command=btn5_function)
btn5.pack(side=LEFT,expand=True,fill='both')

btn6 = Button(btnrow2,text='6',
              font=('Verdana',22),
              relief=GROOVE,border=0,command=btn6_function)
btn6.pack(side=LEFT,expand=True,fill='both')

btnminus = Button(btnrow2,text='-',
                  font=('Verdana',22),
                  relief=GROOVE,border=0,command=btnminus_function)
btnminus.pack(side=LEFT,expand=True,fill='both')

#  ---------- third line of buttons goes here -------------

btn7 = Button(btnrow3,text='7',
              font=('Verdana',22),
              relief=GROOVE,border=0,command=btn7_function)
btn7.pack(side=LEFT,expand=True,fill='both')

btn8 = Button(btnrow3,text='8',
              font=('Verdana',22),
              relief=GROOVE,border=0,command=btn8_function)
btn8.pack(side=LEFT,expand=True,fill='both')

btn9 = Button(btnrow3,text='9',font=('Verdana',22),relief=GROOVE,border=0,command=btn9_function)
btn9.pack(side=LEFT,expand=True,fill='both')

btnmultiply = Button(btnrow3,text='x',font=('Verdana',22),
                     relief=GROOVE,border=0,command=btnmutiply_function)
btnmultiply.pack(side=LEFT,expand=True,fill='both')

# --------- fourth line of buttons goes here ----------

btndot = Button(btnrow4,text='.',font=('Verdana',22),relief=GROOVE,border=0,command=btndot_function)
btndot.pack(side=LEFT,expand=True,fill='both')

btn0 = Button(btnrow4,text='0',font=('Verdana',22),relief=GROOVE,border=0,command=btn0_function)
btn0.pack(side=LEFT,expand=True,fill='both')

btndivide = Button(btnrow4,text='/',font=('Verdana',22),
                   relief=GROOVE,border=0,command=btndivide_function)
btndivide.pack(side=LEFT,expand=True,fill='both')

btnequal = Button(btnrow4,text='=',font=('Verdana',22),
                  relief=GROOVE,border=0,command=equalbtn_function)
btnequal.pack(side=LEFT,expand=True,fill='both')

window.mainloop()