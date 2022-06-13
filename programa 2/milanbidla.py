########################################################################################################################

from tkinter import *
from random import randint
from tkinter import messagebox

########################################################################################################################

tk = Tk()

########################################################################################################################

count=0

########################################################################################################################

def trans():
    global count
    count+=1

########################################################################################################################

def menu():
    global tk
    global count
    count=0
    tk.destroy()
    tk = Tk()


    tk.title("EasyMath // by bagai35 , fuunzap")
    tk.geometry("1500x890")

    c = Canvas(tk, bg="gray", height=100, width=200)
    filename = PhotoImage(file="background.png")
    background_label = Label(tk, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    c.pack()

    img = PhotoImage(file='logo3.png')
    Label(tk, image=img).pack()


    data = StringVar()
    data.set("Приветствуем, это программа создана для быстрого счёта\n"
             "Выберите действие, которое будете тренировать")

    label = Label(textvariable=data)
    label.place(x=555, y=280)

    btn1 = Button(text="Сложение", background="#D39E5A", foreground="#FFFFFF", padx="17",
                  pady="1", font="1", command=click1)
    btn1.place(x=495, y=460)

    btn2 = Button(text="Вычитание", background="#D39E5A", foreground="#FFFFFF", padx="17",
                  pady="1", font="1", command=click2)
    btn2.place(x=620, y=460)

    btn3 = Button(text="Умножение", background="#D39E5A", foreground="#FFFFFF", padx="17",
                  pady="1", font="1", command=click3)
    btn3.place(x=750, y=460)

    btn4 = Button(text="Деление", background="#D39E5A", foreground="#FFFFFF", padx="17",
                  pady="1", font="1", command=click4)
    btn4.place(x=885, y=460)
    
    tk.mainloop()

########################################################################################################################

def click1():
    global tk
    global f1, f2, f3, f4, f5
    global c1, c2, c3, c4, c5
    tk.destroy()
    tk=Tk()
    global count
    tk.geometry("800x600")
    tk.title = ('сложение')
    tk.configure(bg="gray")
    a1 = randint(1, 100)
    b1 = randint(1, 100)
    a2 = randint(1, 100)
    b2 = randint(1, 100)
    a3 = randint(1, 100)
    b3 = randint(1, 100)
    a4 = randint(1, 100)
    b4 = randint(1, 100)
    a5 = randint(1, 100)
    b5 = randint(1, 100)

    c1 = a1 + b1
    c2 = a2 + b2
    c3 = a3 + b3
    c4 = a4 + b4
    c5 = a5 + b5

    f1 = randint(1, 10)
    f2 = randint(1, 10)
    f3 = randint(1, 10)
    f4 = randint(1, 10)
    f5 = randint(1, 10)

    less1=StringVar()
    less1.set("{0}+{1}=".format(a1,b1))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=100)

    less1=StringVar()
    less1.set("{0}+{1}=".format(a2,b2))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=150)

    less1=StringVar()
    less1.set("{0}+{1}=".format(a3,b3))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=200)

    less1=StringVar()
    less1.set("{0}+{1}=".format(a4,b4))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=250)

    less1=StringVar()
    less1.set("{0}+{1}=".format(a5,b5))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=300)

########################################################################################################################

    lang=IntVar()
    ans11 = Radiobutton(text=c1, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans12 = Radiobutton(text=f1, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans21 = Radiobutton(text=c2, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans22 = Radiobutton(text=f2, value=2, variable=lang, padx=1, pady=1)
    lang=IntVar()
    ans13 = Radiobutton(text=c3, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans23 = Radiobutton(text=f3, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans14 = Radiobutton(text=c4, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans24 = Radiobutton(text=f4, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans15 = Radiobutton(text=c5, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans25 = Radiobutton(text=f5, value=2, variable=lang, padx=1, pady=1)

    ans11.place(x=300, y=100)
    ans12.place(x=350, y=100)
    ans21.place(x=300, y=150)
    ans22.place(x=350, y=150)
    ans13.place(x=300, y=200)
    ans23.place(x=350, y=200)
    ans14.place(x=300, y=250)
    ans24.place(x=350, y=250)
    ans15.place(x=300, y=300)
    ans25.place(x=350, y=300)

    btn5 = Button(text='OK', background="#D39E5A", foreground="#FFFFFF", padx='17',
                  pady="1", font="1", command=mb)
    btn5.place(x=500, y=500)


    tk.mainloop()

########################################################################################################################

def click2():
    global tk
    global f1, f2, f3, f4, f5
    global c1, c2, c3, c4, c5
    tk.destroy()
    tk=Tk()
    tk.title=('вычитание')
    tk.geometry("800x600")
    tk.configure(bg="skyblue")
    a1 = randint(1, 100)
    b1 = randint(1, 100)
    a2 = randint(1, 100)
    b2 = randint(1, 100)
    a3 = randint(1, 100)
    b3 = randint(1, 100)
    a4 = randint(1, 100)
    b4 = randint(1, 100)
    a5 = randint(1, 100)
    b5 = randint(1, 100)

    c1 = a1 - b1
    c2 = a2 - b2
    c3 = a3 - b3
    c4 = a4 - b4
    c5 = a5 - b5

    f1 = randint(1, 10)
    f2 = randint(1, 10)
    f3 = randint(1, 10)
    f4 = randint(1, 10)
    f5 = randint(1, 10)

    less1 = StringVar()
    less1.set("{0}-{1}=".format(a1, b1))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=100)

    less1 = StringVar()
    less1.set("{0}-{1}=".format(a2, b2))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=150)

    less1 = StringVar()
    less1.set("{0}-{1}=".format(a3, b3))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=200)

    less1 = StringVar()
    less1.set("{0}-{1}=".format(a4, b4))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=250)

    less1 = StringVar()
    less1.set("{0}-{1}=".format(a5, b5))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=300)


########################################################################################################################

    lang = IntVar()
    ans11 = Radiobutton(text=c1, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans12 = Radiobutton(text=f1, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans21 = Radiobutton(text=c2, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans22 = Radiobutton(text=f2, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans13 = Radiobutton(text=c3, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans23 = Radiobutton(text=f3, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans14 = Radiobutton(text=c4, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans24 = Radiobutton(text=f4, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans15 = Radiobutton(text=c5, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans25 = Radiobutton(text=f5, value=2, variable=lang, padx=1, pady=1)

    ans11.place(x=300, y=100)
    ans12.place(x=350, y=100)
    ans21.place(x=300, y=150)
    ans22.place(x=350, y=150)
    ans13.place(x=300, y=200)
    ans23.place(x=350, y=200)
    ans14.place(x=300, y=250)
    ans24.place(x=350, y=250)
    ans15.place(x=300, y=300)
    ans25.place(x=350, y=300)

    btn5 = Button(text='OK', background="#D39E5A", foreground="#FFFFFF", padx='17',
                  pady="1", font="1", command=mb)
    btn5.place(x=500, y=500)

    tk.mainloop()

########################################################################################################################

def click3():
    global tk
    global f1, f2, f3, f4, f5
    global c1, c2, c3, c4, c5
    tk.destroy()
    tk=Tk()
    tk.title=('умножение')
    tk.geometry("800x600")
    tk.configure(bg="pink")
    a1 = randint(1, 10)
    b1 = randint(1, 10)
    a2 = randint(1, 10)
    b2 = randint(1, 10)
    a3 = randint(1, 10)
    b3 = randint(1, 10)
    a4 = randint(1, 10)
    b4 = randint(1, 10)
    a5 = randint(1, 10)
    b5 = randint(1, 10)

    c1 = a1 * b1
    c2 = a2 * b2
    c3 = a3 * b3
    c4 = a4 * b4
    c5 = a5 * b5

    f1 = randint(1, 10)
    f2 = randint(1, 10)
    f3 = randint(1, 10)
    f4 = randint(1, 10)
    f5 = randint(1, 10)

    less1 = StringVar()
    less1.set("{0}х{1}=".format(a1, b1))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=100)

    less1 = StringVar()
    less1.set("{0}х{1}=".format(a2, b2))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=150)

    less1 = StringVar()
    less1.set("{0}х{1}=".format(a3, b3))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=200)

    less1 = StringVar()
    less1.set("{0}х{1}=".format(a4, b4))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=250)

    less1 = StringVar()
    less1.set("{0}х{1}=".format(a5, b5))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=300)

########################################################################################################################

    lang = IntVar()
    ans11 = Radiobutton(text=c1, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans12 = Radiobutton(text=f1, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans21 = Radiobutton(text=c2, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans22 = Radiobutton(text=f2, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans13 = Radiobutton(text=c3, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans23 = Radiobutton(text=f3, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans14 = Radiobutton(text=c4, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans24 = Radiobutton(text=f4, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans15 = Radiobutton(text=c5, value=1, variable=lang, padx=1, pady=1, command=trans)
    ans25 = Radiobutton(text=f5, value=2, variable=lang, padx=1, pady=1)

    ans11.place(x=300, y=100)
    ans12.place(x=350, y=100)
    ans21.place(x=300, y=150)
    ans22.place(x=350, y=150)
    ans13.place(x=300, y=200)
    ans23.place(x=350, y=200)
    ans14.place(x=300, y=250)
    ans24.place(x=350, y=250)
    ans15.place(x=300, y=300)
    ans25.place(x=350, y=300)

    btn5 = Button(text='OK', background="#D39E5A", foreground="#FFFFFF", padx='17',
                  pady="1", font="1", command=mb)
    btn5.place(x=500, y=500)
    tk.mainloop()

########################################################################################################################

def click4():
    global tk

    global tk
    global f1, f2, f3, f4, f5
    global c1, c2, c3, c4, c5
    tk.destroy()
    tk=Tk()
    tk.title=('деление')
    tk.geometry("800x600")
    tk.configure(bg="yellow")
    a1 = randint(1, 10)
    b1 = randint(1, 10)
    a2 = randint(1, 10)
    b2 = randint(1, 10)
    a3 = randint(1, 10)
    b3 = randint(1, 10)
    a4 = randint(1, 10)
    b4 = randint(1, 10)
    a5 = randint(1, 10)
    b5 = randint(1, 10)

    c1 = a1 / b1
    c2 = a2 / b2
    c3 = a3 / b3
    c4 = a4 / b4
    c5 = a5 / b5
    

    f1 = randint(1, 10)
    f2 = randint(1, 10)
    f3 = randint(1, 10)
    f4 = randint(1, 10)
    f5 = randint(1, 10)

    less1 = StringVar()
    less1.set("{0}:{1}=".format(a1, b1))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=100)

    less1 = StringVar()
    less1.set("{0}:{1}=".format(a2, b2))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=150)

    less1 = StringVar()
    less1.set("{0}:{1}=".format(a3, b3))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=200)

    less1 = StringVar()
    less1.set("{0}:{1}=".format(a4, b4))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=250)

    less1 = StringVar()
    less1.set("{0}:{1}=".format(a5, b5))
    label1 = Label(textvariable=less1)
    label1.place(x=250, y=300)

########################################################################################################################

    lang = IntVar()
    ans11 = Radiobutton(text=round(c1, 2), value=1, variable=lang, padx=1, pady=1, command=trans)
    ans12 = Radiobutton(text=f1, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans21 = Radiobutton(text=round(c2, 2), value=1, variable=lang, padx=1, pady=1, command=trans)
    ans22 = Radiobutton(text=f2, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans13 = Radiobutton(text=round(c3, 2), value=1, variable=lang, padx=1, pady=1, command=trans)
    ans23 = Radiobutton(text=f3, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans14 = Radiobutton(text=round(c4, 2), value=1, variable=lang, padx=1, pady=1, command=trans)
    ans24 = Radiobutton(text=f4, value=2, variable=lang, padx=1, pady=1)
    lang = IntVar()
    ans15 = Radiobutton(text=round(c5, 2), value=1, variable=lang, padx=1, pady=1, command=trans)
    ans25 = Radiobutton(text=f5, value=2, variable=lang, padx=1, pady=1)

    ans11.place(x=300, y=100)
    ans12.place(x=350, y=100)
    ans21.place(x=300, y=150)
    ans22.place(x=350, y=150)
    ans13.place(x=300, y=200)
    ans23.place(x=350, y=200)
    ans14.place(x=300, y=250)
    ans24.place(x=350, y=250)
    ans15.place(x=300, y=300)
    ans25.place(x=350, y=300)

    btn5 = Button(text='OK', background="#D39E5A", foreground="#FFFFFF", padx='17',
                  pady="1", font="1", command=mb)
    btn5.place(x=500, y=500)
    tk.mainloop()

########################################################################################################################

def mb():
    print(count)
    messagebox.showinfo(title='end', message='Решено {0} из 5 примеров'.format(count))
    menu()

########################################################################################################################

menu()

########################################################################################################################
