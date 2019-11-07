from tkinter import *
import time
import random
import RPi.GPIO as GPIO
 
# Sets the pin numbers for the buttons
L_Add = 23 # 18 # Adds 1 to Count1
R_Add = 4 # 23 # Adds 1 to Count2
L_Sub = 24 # 24 # Subtracts 1 from Count1
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

PHOTO = PhotoImage(file="NOTAJPG!.png")

mainframe = Frame(root)
mainframe["bg"] = 'black'
mainframe.grid(column=3, row=3, sticky=(N, W, E, S)) # Sets up the grid

mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

Font_Size = 9
Font_Family = 'Consolas'
padx_Size = 125
pady_Size = 100

# Row 0

Answer1 = StringVar()
Answer1.set('DOG')

Answer1_Label = Label(mainframe,textvariable=Answer1,bg='black',fg='gold', font=f'Hack 20')
Answer1_Label.grid(row=1, column=0, padx=padx_Size, pady=pady_Size)

photo_label = Label(mainframe, image=PHOTO)
photo_label.grid(row=1, column = 1, padx=padx_Size, pady=pady_Size)

 
Answer2 = StringVar()
Answer2.set("CAT")

Answer2_Label = Label(mainframe,textvariable=Answer2,bg='black',fg='gold', font=f'Hack 20')
Answer2_Label.grid(row=1,column=2,padx=padx_Size, pady=pady_Size)

# Row 2

Count1 = StringVar()
Count1.set('0')

Count1_Label = Label(mainframe,textvariable=Count1,bg='black',fg='gold', font=f'Hack 60 bold')
Count1_Label.grid(row=2, column=0, padx=padx_Size, pady=pady_Size)

Question = StringVar()
Question.set('WHICH IS YOUR FAVORITE ANIMAL?')

Question_Label = Label(mainframe,textvariable=Question,bg='black',fg='gold', font=f'Hack 30')
Question_Label.grid(row=2, column=1,padx=padx_Size, pady=pady_Size)

Count2 = StringVar()
Count2.set("0")

Count2_Label = Label(mainframe,textvariable=Count2,bg='black',fg='gold', font=f'Hack 60 bold')
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
    for x in range(2):
        change_color('black','gold')
        time.sleep(0.5)    
        change_color('gold','black')
        time.sleep(0.5)
    Finish_Value = random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit)

# Changes the color of the text and background
def change_color(color, color2): # change_color(NewTextColor, NewBackgroundColor)
    Question_Label.config(fg=color, bg=color2)
    Count1_Label.config(fg=color, bg=color2)
    Count2_Label.config(fg=color, bg=color2)
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

