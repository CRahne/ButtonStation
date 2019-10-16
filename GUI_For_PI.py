from tkinter import *
import time
import keyboard # Tools -> Manage Packages -> keyboard -> Install

# Also I found a good video of how to do something
# similar to what we are doing:
# https://www.youtube.com/watch?v=dQw4w9WgXcQ

 
root = Tk()
root.geometry('1000x500+20+20')
 
mainframe = Frame(root)
mainframe.grid(column=1000, row=1000, sticky=(N, W, E, S))

mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

Font_Size = 12

# Row 0

Title_String = StringVar()
Title_String.set("This is my great title")

Title_Label = Label(mainframe,textvariable=Title_String,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Title_Label.grid(row=0, column=1, padx=50)
 
Team_Number = StringVar()
Team_Number.set("2509")

Team_Number_L = Label(mainframe,textvariable=Team_Number,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Team_Number_L.grid(row=0, column=0, padx=50)
 
Team_Number_R = Label(mainframe,textvariable=Team_Number,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Team_Number_R.grid(row=0, column=2, padx=50)

# Row 1

Answer1 = StringVar()
Answer1.set('Woofer')

Answer1_Label = Label(mainframe,textvariable=Answer1,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Answer1_Label.grid(row=1, column=0, padx=50)

Question = StringVar()
Question.set('Which animal')

Question_Label = Label(mainframe,textvariable=Question,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Question_Label.grid(row=1, column=1,padx=50)

Answer2 = StringVar()
Answer2.set("Meower")

Answer2_Label = Label(mainframe,textvariable=Answer2,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Answer2_Label.grid(row=1,column=2,padx=50)

 
Count1 = StringVar()
Count1.set('start')

Count1_Label = Label(mainframe,textvariable=Count1,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Count1_Label.grid(row=2, column=0, padx=50)

Middle = StringVar()
Middle.set('start2')

Middle_Label = Label(mainframe,textvariable=Middle,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Middle_Label.grid(row=2, column=1,padx=50)

Count2 = StringVar()
Count2.set("image")

Count2_Label = Label(mainframe,textvariable=Count2,bg='#321000',fg='#000fff000',font=("Helvetica",Font_Size))
Count2_Label.grid(row=2,column=2,padx=50)
 
def run(n, i, master):
    Count1.set('%d' % (n))
    Count2.set('%d' % (i))
    if keyboard.is_pressed('q'):
        n += 1
        time.sleep(0.1)
    if keyboard.is_pressed('w'):
        i += 1
        time.sleep(0.1)
    if n <= 10 or i <= 10:
        mainframe.after(1, run, n, i, master)
    else:
        i = 0
        n = 0
        Title_String.set("Wow U R Cool")
        mainframe.after(1, run, n, i, master)

run(0, 0, mainframe)
root.mainloop()