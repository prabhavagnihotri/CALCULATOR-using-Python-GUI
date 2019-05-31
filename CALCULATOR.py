#Calculator like windows


from tkinter import *
root = Tk()
root.title('CALCULATOR')
root.iconbitmap('calc.ico')
# root.state('zoomed')
root.geometry('320x400')
root.resizable(0,0)
root.config(background = 'lawn green')
a = ""
txt_input = StringVar()


def get_value(numbers):
    global a
    a = a + str(numbers)
    txt_input.set(a)

def clear_value():
    global a
    a = ""
    txt_input.set("")

def equal_button():
    global a
    s = str(eval(a))
    txt_input.set(s)
    a = ""

txt = Entry(root,width = 15 ,text = txt_input,fg = 'black',bg = 'white',font = ('times',25,'bold'))
txt.place(x = 30 , y = 80)

btn1 = Button(root,text = '1',command = lambda:get_value(1),width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn1.place(x = 30, y = 200)

btn2 = Button(root,text = '2',command = lambda:get_value(2) ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn2.place(x = 100, y = 200)

btn3 = Button(root,text = '3',command = lambda:get_value(3) ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn3.place(x = 170, y = 200)

btn4 = Button(root,text = '4',command = lambda:get_value(4),width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn4.place(x = 30, y = 250)

btn5 = Button(root,text = '5',command = lambda:get_value(5) ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn5.place(x = 100, y = 250)

btn6 = Button(root,text = '6',command = lambda:get_value(6),width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn6.place(x = 170, y = 250)

btn7 = Button(root,text = '7',command = lambda:get_value(7) ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn7.place(x = 30, y = 300)

btn8 = Button(root,text = '8',command = lambda:get_value(8),width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn8.place(x = 100, y = 300)

btn9 = Button(root,text = '9',command = lambda:get_value(9) ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn9.place(x = 170, y = 300)

btn0 = Button(root,text = '0',command = lambda:get_value(0),width = 17,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn0.place(x = 30, y = 350)

btn_add = Button(root,text='+',command = lambda:get_value('+') ,width = 5,fg = 'black',bg = 'cyan',height = 8,font = ('times new roman',10,'bold'))
btn_add.place(x = 244, y = 150)

btn_sub = Button(root,text='-',command = lambda:get_value('-') ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn_sub.place(x = 170, y = 150)

btn_mul = Button(root,text='*',command = lambda:get_value('*') ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn_mul.place(x = 100, y = 150)

btn_div = Button(root,text='/',command = lambda:get_value('/') ,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn_div.place(x = 30, y = 150)


btn_clear = Button(root,text = 'C',command = clear_value,width = 5,fg = 'black',bg = 'cyan',height = 5,font = ('times new roman',10,'bold'))
btn_clear.place(x = 244, y = 292)

btn_equals = Button(root,text = '=',command = equal_button,width = 7,fg = 'black',bg = 'cyan',height = 1,font = ('times new roman',10,'bold'))
btn_equals.place(x = 170, y = 350)


def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel('quit','press ok if quit'):
        root.destroy()
root.protocol('WM_DELETE_WINDOW',on_closing)

root.mainloop()