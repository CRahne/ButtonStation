from tkinter import *
import time
# import keyboard

ROBOT2018 = """|-------\                         
| |----\ \                        
| |     \ \        |------------| 
|2|      \ \       |            | 
|5|       \ \      |            | 
|0|        \ \     |    [--]    | 
|9|         \ \    |    [--]    | 
| |          \ \   |----/ /-----| 
|2|-----------\ \------/ /        
|0|------------\ \------/         
|1|             \ \               
|8|              \ \              
| |               \ \             
| |                \ \         |-|
|-------------------\-\--|-----|-|
|.'''.    .'''.    .'''. |     (=)
|------------------------|        
 '...'    '...'    '...'          """


ROBOT2019 = """
              /--|
             /   |
            / /| |
           / / |2|
          / /  |5|
   /-----/ /   |0|
  /     / /    |9|
 /     / /     | |
                   /     / /      |2|         |----_-(0)
              \    / /       |0|         | ,-'
            \  / /        |1|---------|/
            \/ /         |9|---------|
            / /  |-----| | |         |
           / /   |     | | |         |
               / /  __|_____|_|_|         | '-._
                    /.'''. || .'''. || .'''.    |-----¯---._
     |------------------------|
      '...'    '...'    '...' """
 
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
     22                  55   00      00          99 
   22                   55     00    00           99 
  22222222222    5555555       000000            99"""
 
 
root = Tk()
root.geometry('1020x710+0+0') # My Laptop. Go to Windows -> Display Settings -> Resolution
root.configure(bg='black')
 
mainframe = Frame(root)
mainframe["bg"] = 'black'
mainframe.grid(column=3, row=3, sticky=(N, W, E, S))

mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

Font_Size = 9
Font_Family = 'Consolas'
padx_Size = 50
pady_Size = 20

# Row 0

Title_String = StringVar()
Title_String.set(HUTCH2509)

#Title_Label = Label(mainframe,textvariable=Title_String,bg='black',fg='gold',font=("Helvetica", Font_Size))
Title_Label = Label(mainframe,textvariable=Title_String,bg='black',fg='gold',font=f'{Font_Family} {Font_Size} bold')
Title_Label.grid(row=0, column=1, padx=padx_Size, pady=pady_Size)
 
Team_Number = StringVar()
Team_Number.set("! TIGERBOTS !")

Team_Number_L = Label(mainframe, textvariable=Team_Number, bg='black', fg='gold',  font=f'{Font_Family} {Font_Size} bold')
Team_Number_L.grid(row=0, column=0, padx=padx_Size, pady=pady_Size)
 
Team_Number_R = Label(mainframe,textvariable=Team_Number,bg='black',fg='gold', font=f'{Font_Family} {Font_Size} bold')
Team_Number_R.grid(row=0, column=2, padx=padx_Size, pady=pady_Size)

# Row 1

Answer1 = StringVar()
Answer1.set('DOG')

Answer1_Label = Label(mainframe,textvariable=Answer1,bg='black',fg='gold', font=f'Hack 20')
Answer1_Label.grid(row=1, column=0, padx=padx_Size, pady=pady_Size)

Middle = StringVar()
Middle.set(ROBOT2018)

Middle_Label = Label(mainframe,textvariable=Middle,bg='black',fg='gold', font=f'{Font_Family} 8')
Middle_Label.grid(row=1, column=1,padx=padx_Size, pady=pady_Size)

Answer2 = StringVar()
Answer2.set("CAT")

Answer2_Label = Label(mainframe,textvariable=Answer2,bg='black',fg='gold', font=f'Hack 20')
Answer2_Label.grid(row=1,column=2,padx=padx_Size, pady=pady_Size)

 # Row 2
 
Count1 = StringVar()
Count1.set('start')

Count1_Label = Label(mainframe,textvariable=Count1,bg='black',fg='gold', font=f'Hack 35')
Count1_Label.grid(row=2, column=0, padx=padx_Size, pady=pady_Size)

Question = StringVar()
Question.set('Which is your favorite animal?')

Question_Label = Label(mainframe,textvariable=Question,bg='black',fg='gold', font=f'Hack 22')
Question_Label.grid(row=2, column=1,padx=padx_Size, pady=pady_Size)

Count2 = StringVar()
Count2.set("start")

Count2_Label = Label(mainframe,textvariable=Count2,bg='black',fg='gold', font=f'Hack 35')
Count2_Label.grid(row=2,column=2,padx=padx_Size, pady=pady_Size)
s
root.mainloop()
