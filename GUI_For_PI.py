from tkinter import *
import time
import keyboard

 
root = Tk()
root.geometry('1000x500+20+20')
 
mainframe = Frame(root)
mainframe.grid(column=1000, row=1000, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
 
best = StringVar()
best.set('start')

best2 = StringVar()
best2.set('start2')

best3 = StringVar()
best3.set("image")

x1 = 12

label1 = Label(mainframe,textvariable=best,bg='#321000',fg='#000fff000',font=("Helvetica",x1))
label1.grid(row=1, column=0, padx=50)

label3 = Label(mainframe,textvariable=best3,bg='#321000',fg='#000fff000',font=("Helvetica",x1))
label3.grid(row=1, column=1,padx=50)

label2 = Label(mainframe,textvariable=best2,bg='#321000',fg='#000fff000',font=("Helvetica",x1))
label2.grid(row=1,column=2,padx=50)
 
def run(n, i, master):
    best.set('test # %d' % (n))
    best2.set(f'test2 # {i}')
    if keyboard.is_pressed('q'):
        n += 1
    if keyboard.is_pressed('w'):
        i += 1
    if n <= 10 or i <= 10:
        mainframe.after(100, run, n, i, master)

run(0, 0, mainframe)
root.mainloop()
while True:
    best.set('testestes')
    root.update()