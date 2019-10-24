from tkinter import *
import time
import random
import RPi.GPIO as GPIO

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
 
# Sets the pin numbers for the buttons
L_Add = 24 # 18 # Adds 1 to Count1
R_Add = 4 # 23 # Adds 1 to Count2
L_Sub = 23 # 24 # Subtracts 1 from Count1
R_Sub = 18 # 25 # Subtracts 1 from Count2
Auto_Finish = 25 # 4 # Finishes the game

GPIO.setmode(GPIO.BCM)
GPIO.setup(L_Add, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_Add, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_Sub, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_Sub, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Auto_Finish, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Finish_Value_Upper_Limit = 25
Finish_Value_Lower_Limit = 5
Finish_Value = random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit) # Determines when the program will restart

root = Tk()
root.geometry('1600x900+0+0') # Sets the Resolution. My Laptop. Go to Windows -> Display Settings -> Resolution
root.configure(bg='black')
 
mainframe = Frame(root)
mainframe["bg"] = 'black'
mainframe.grid(column=3, row=3, sticky=(N, W, E, S)) # Sets up the grid

mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

Font_Size = 9
Font_Family = 'Consolas'
padx_Size = 145
pady_Size = 50

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
Middle.set(ROBOT2019)

Middle_Label = Label(mainframe,textvariable=Middle,bg='black',fg='gold', font=f'{Font_Family} 8')
Middle_Label.grid(row=1, column=1,padx=padx_Size, pady=pady_Size)

Answer2 = StringVar()
Answer2.set("CAT")

Answer2_Label = Label(mainframe,textvariable=Answer2,bg='black',fg='gold', font=f'Hack 20')
Answer2_Label.grid(row=1,column=2,padx=padx_Size, pady=pady_Size)

 # Row 2
 
Count1 = StringVar()
Count1.set('0')

Count1_Label = Label(mainframe,textvariable=Count1,bg='black',fg='gold', font=f'Hack 35')
Count1_Label.grid(row=2, column=0, padx=padx_Size, pady=pady_Size)

Question = StringVar()
Question.set('WHICH IS YOUR FAVORITE ANIMAL?')

Question_Label = Label(mainframe,textvariable=Question,bg='black',fg='gold', font=f'Hack 20')
Question_Label.grid(row=2, column=1,padx=padx_Size, pady=pady_Size)

Count2 = StringVar()
Count2.set("0")

Count2_Label = Label(mainframe,textvariable=Count2,bg='black',fg='gold', font=f'Hack 35')
Count2_Label.grid(row=2,column=2,padx=padx_Size, pady=pady_Size)

# Runs whenever a button is pressed
def buttonPress(channel):
    global Finish_Value
    if (int(Count1.get()) == Finish_Value and channel == L_Add) or (int(Count2.get()) == Finish_Value and channel == R_Add) or channel == Auto_Finish:
        finish()
    elif channel == L_Add: # Adds 1 to Count1
        Count1.set(int(Count1.get()) + 1)
    elif channel == R_Add: # Adds 1 to Count2
        Count2.set(int(Count2.get()) + 1)
    elif (channel == L_Sub) and (int(Count1.get()) > 0): # Subtracts 1 from Count1 if it is greater than 0
        # print(int(Count1.get()))
        Count1.set(int(Count1.get()) - 1)
    elif(channel == R_Sub) and (int(Count2.get()) > 0): # Subtracts 1 from the Count2 if it is greater than 0
        # print(int(Count2.get()))
        Count2.set(int(Count2.get()) - 1)
    else:
        pass

# Runs when either Count is equal to Finish_Value. Resets the Counts and briefly changes the color of the screen
def finish():
    global Finish_Value
    Count1.set('0')
    Count2.set('0')
    for Value in range(3):
        change_color('black','gold')
        time.sleep(0.5)    
        change_color('gold','black')
        time.sleep(0.5)
    Finish_Value = random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit)

# Changes the color of the text and background
def change_color(color, color2): # change_color(NewTextColor, NewBackgroundColor)
    Middle_Label.config(fg=color, bg=color2)
    Title_Label.config(fg=color, bg=color2)
    Question_Label.config(fg=color, bg=color2)
    Count1_Label.config(fg=color, bg=color2)
    Count2_Label.config(fg=color, bg=color2)
    Team_Number_L.config(fg=color, bg=color2)
    Team_Number_R.config(fg=color, bg=color2)
    Middle_Label.config(fg=color, bg=color2)
    Answer1_Label.config(fg=color, bg=color2)
    Answer2_Label.config(fg=color, bg=color2)
    mainframe["bg"] = color2
    root.configure(bg=color2)
    

# Adds event catchers for the buttons
GPIO.add_event_detect(L_Add, GPIO.RISING, callback=buttonPress, bouncetime=300)
GPIO.add_event_detect(R_Add, GPIO.RISING, callback=buttonPress, bouncetime=300)
GPIO.add_event_detect(L_Sub, GPIO.RISING, callback=buttonPress, bouncetime=300)
GPIO.add_event_detect(R_Sub, GPIO.RISING, callback=buttonPress, bouncetime=300)
GPIO.add_event_detect(Auto_Finish, GPIO.RISING, callback=buttonPress, bouncetime=300)


# run(0, 0, mainframe)
root.mainloop()
GPIO.cleanup()
