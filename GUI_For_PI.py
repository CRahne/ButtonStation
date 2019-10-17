from tkinter import *
import time
import keyboard # Tools -> Manage Packages -> keyboard -> Install

# Also I found a good video of how to do something
# similar to what we are doing:
# https://www.youtube.com/watch?v=dQw4w9WgXcQ

 
HUTCH2509 = """
 |---|    |---|   |---|  |---|  |-----------|   /-------\  |---|    |---|
 |   |    |   |   |   |  |   |  |           |  /  /-----/  |   |    |   |
 |   |----|   |   |   |  |   |  |---|   |---|  |  |        |   |----|   |
 |            |   |   |  |   |      |   |      |  |        |            |
 |   |----|   |   |   \--/   |      |   |      |  |        |   |----|   |
 |   |    |   |   \          /      |   |      \  \-----\  |   |    |   |
 |---|    |---|    \--------/       |---|       \-------/  |---|    |---|

    222222222    55555555      000000     999999999
   22       22   55           00    00    99     99
           22    55          00      00   99     99
         22      5555555     00      00   99     99
       22              55    00      00   999999999
     22                 55   00      00          99 
   22                  55     00    00           99 
  22222222222    5555555       000000            99"""
 
 
root = Tk()
root.geometry('1000x500+20+20')
root.configure(bg='black')
 
mainframe = Frame(root)
mainframe["bg"] = 'black'
mainframe.grid(column=1000, row=1000, sticky=(N, W, E, S))

mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

Font_Size = 11
Font_Family = 'Consolas'

# Row 0

Title_String = StringVar()
Title_String.set(HUTCH2509)

#Title_Label = Label(mainframe,textvariable=Title_String,bg='black',fg='gold',font=("Helvetica", Font_Size))
Title_Label = Label(mainframe,textvariable=Title_String,bg='black',fg='gold',font=f'{Font_Family} {Font_Size} bold')
Title_Label.grid(row=0, column=1, padx=50)
 
Team_Number = StringVar()
Team_Number.set("! TIGERBOTS !")

Team_Number_L = Label(mainframe, textvariable=Team_Number, bg='black', fg='gold',  font=f'{Font_Family} {Font_Size} bold')
Team_Number_L.grid(row=0, column=0, padx=50)
 
Team_Number_R = Label(mainframe,textvariable=Team_Number,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
Team_Number_R.grid(row=0, column=2, padx=50)

# Row 1

Answer1 = StringVar()
Answer1.set('Woofer')

Answer1_Label = Label(mainframe,textvariable=Answer1,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
Answer1_Label.grid(row=1, column=0, padx=50)

Question = StringVar()
Question.set('Which animal')

Question_Label = Label(mainframe,textvariable=Question,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
Question_Label.grid(row=1, column=1,padx=50)

Answer2 = StringVar()
Answer2.set("Meower")

Answer2_Label = Label(mainframe,textvariable=Answer2,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
Answer2_Label.grid(row=1,column=2,padx=50)

 # Row 2
 
Count1 = StringVar()
Count1.set('start')

Count1_Label = Label(mainframe,textvariable=Count1,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
Count1_Label.grid(row=2, column=0, padx=50)

Middle = StringVar()
Middle.set('start2')

Middle_Label = Label(mainframe,textvariable=Middle,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
Middle_Label.grid(row=2, column=1,padx=50)

Count2 = StringVar()
Count2.set("image")

Count2_Label = Label(mainframe,textvariable=Count2,bg='black',fg='gold', font=f'{Font_Family} {Font_Size}')
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
        master.after(1, run, n, i, master)
    else:
        i = 0
        n = 0
        Title_String.set("Wow U R Cool")
        master.after(100, run, n, i, master)
        
#def run2(n, i,master):

run(0, 0, mainframe)
root.mainloop()