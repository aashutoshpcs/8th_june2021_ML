##CALCULATOR

import tkinter as tk
expr=""
app=tk.Tk()
app.title('CALCULATOR')
app.geometry('320x420')
#app.resizable(0,0)
    
result=tk.Variable(app)
box=tk.Entry(app, textvariable=result, width=42,font=16)
box.place(x=10,y=40,height=50)

def operate(num):
    global expr
    expr= expr+num
    result.set(expr)
    
def clear():
    global expr
    expr=""
    result.set(expr)

def final():
    global expr
    result.set(eval(expr))
    expr=""
    

tk.Button(app, text='Clear', width = 10, height=1, command=lambda: clear()).place(x=18,y=8)
tk.Button(app, text='7', width = 5, height=2, command=lambda: operate('7')).place(x=18,y=105)
tk.Button(app, text='8', width = 5, height=2, command=lambda: operate('8')).place(x=88,y=105)
tk.Button(app, text='9', width = 5, height=2, command=lambda: operate('9')).place(x=160,y=105)
tk.Button(app, text='+', width = 5, height=2, command=lambda: operate('+')).place(x=240,y=105)
tk.Button(app, text='4', width = 5, height=2, command=lambda: operate('4')).place(x=18,y=175)
tk.Button(app, text='5', width = 5, height=2, command=lambda: operate('5')).place(x=88,y=175)
tk.Button(app, text='6', width = 5, height=2, command=lambda: operate('6')).place(x=160,y=175)
tk.Button(app, text='-', width = 5, height=2, command=lambda: operate('-')).place(x=240,y=175)
tk.Button(app, text='1', width = 5, height=2, command=lambda: operate('1')).place(x=18,y=240)
tk.Button(app, text='2', width = 5, height=2, command=lambda: operate('2')).place(x=88,y=240)
tk.Button(app, text='3', width = 5, height=2, command=lambda: operate('3')).place(x=160,y=240)
tk.Button(app, text='*', width = 5, height=2, command=lambda: operate('*')).place(x=240,y=240)
tk.Button(app, text='.', width = 5, height=2, command=lambda: operate('.')).place(x=18,y=310)
tk.Button(app, text='0', width = 5, height=2, command=lambda: operate('0')).place(x=88,y=310)
tk.Button(app, text='=', width = 5, height=2, command=lambda: final()).place(x=160,y=310)
tk.Button(app, text='/', width = 5, height=2, command=lambda: operate('/')).place(x=240,y=310)

app.mainloop()
