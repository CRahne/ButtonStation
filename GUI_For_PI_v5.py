from tkinter import *
import time
import random
import RPi.GPIO as GPIO
import Question_Handler as QH
 
# Sets the pin numbers for the buttons
L_Add = 23 # 18 # Adds 1 to Count1
R_Add = 25 # 23 # Adds 1 to Count2
L_Sub = 24 # 24 # Subtracts 1 from Count1
R_Sub = 18 # 25 # Subtracts 1 from Count2
Auto_Finish = 4 # 4 # Finishes the game

# Sets up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(L_Add, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_Add, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_Sub, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_Sub, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Auto_Finish, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Determines when the program will restart
Finish_Value_Upper_Limit = 25
Finish_Value_Lower_Limit = 5
Finish_Value = random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit)
 
root = Tk()
root.geometry('1600x900+0+0') # Sets the Resolution. My Laptop. Go to Windows -> Display Settings -> Resolution
root.configure(bg='black') # Sets the background of the root window to black. bg = background, fg = foreground

PHOTO = PhotoImage(file="logo350.png") #Gets the image to display. Images must be in .png format

mainframe = Frame(root)
mainframe["bg"] = 'black' # Sets the mainframe background color to black
mainframe.grid(column=3, row=3, sticky=(N, W, E, S)) # Sets up the grid

# Sets up the rows and columns of the grids
mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

Font_Size = 9
Font_Family = 'Consolas'
padx_Size = 0
pady_Size = 100

# Row 1

Start_Question = QH.getRandomQuestion()

Answer1 = StringVar()
Answer1.set(Start_Question[1])

Answer1_Label = Label(mainframe,textvariable=Answer1,bg='black',fg='gold', font=f'Consolas 45 bold')# hack 60
Answer1_Label.grid(row=1, column=0, padx=15, pady=pady_Size)

photo_label = Label(mainframe, image=PHOTO, bg='black')
photo_label.grid(row=1, rowspan = 2, column = 1, sticky = W+E+N+S,padx=80) #padx=padx_Size, pady=0

 
Answer2 = StringVar()
Answer2.set(Start_Question[2])

Answer2_Label = Label(mainframe,textvariable=Answer2,bg='black',fg='gold', font=f'Consolas 45 bold') # hack 60
Answer2_Label.grid(row=1,column=2,padx=15, pady=pady_Size)

# Row 2

Count1 = StringVar()
Count1.set('00')

Count1_Label = Label(mainframe,textvariable=Count1,bg='black',fg='gold', font=f'Hack 120 bold')
Count1_Label.grid(row=2, column=0, padx=padx_Size, pady=pady_Size)

Question = StringVar()
Question.set(Start_Question[0])

Count2 = StringVar()
Count2.set("00")

Count2_Label = Label(mainframe,textvariable=Count2,bg='black',fg='gold', font=f'Hack 120 bold')
Count2_Label.grid(row=2,column=2,padx=padx_Size, pady=pady_Size)

# Row 3

Question_Label = Label(mainframe,textvariable=Question,bg='black',fg='gold', font=f'Consolas 60 bold')
Question_Label.grid(row=3, column=0, columnspan = 3, sticky=W+E+N+S) #padx=padx_Size, pady=pady_Size

# Runs whenever a button is pressed
def buttonPress(channel):
    global Finish_Value
    if (int(Count1.get()) == Finish_Value and channel == L_Add) or (int(Count2.get()) == Finish_Value and channel == R_Add) or channel == Auto_Finish:
        finish()
    elif channel == L_Add: # Adds 1 to Count1
        Count1.set(convert_number(int(Count1.get()) + 1))
    elif channel == R_Add: # Adds 1 to Count2
        Count2.set(convert_number(int(Count2.get()) + 1))
    elif (channel == L_Sub) and (int(Count1.get()) > 0): # Subtracts 1 from Count1 if it is greater than 0
        # print(int(Count1.get()))
        Count1.set(convert_number(int(Count1.get()) - 1))
    elif(channel == R_Sub) and (int(Count2.get()) > 0): # Subtracts 1 from the Count2 if it is greater than 0
        # print(int(Count2.get()))
        Count2.set(convert_number(int(Count2.get()) - 1))
    else:
        pass

# Runs when either Count is equal to Finish_Value. Resets the Counts and briefly changes the color of the screen
def finish():
    global Finish_Value
    Count1.set('00')
    Count2.set('00')
    for x in range(2):
        change_color('black','gold')
        time.sleep(0.5)    
        change_color('gold','black')
        time.sleep(0.5)
    Finish_Value = random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit)

    New_Question = QH.getRandomQuestion()
    Question.set(New_Question[0])
    Answer1.set(New_Question[1])
    Answer2.set(New_Question[2])


# Changes the color of the text and background
def change_color(color, color2): # change_color(NewTextColor, NewBackgroundColor)
    Question_Label.config(fg=color, bg=color2)
    Count1_Label.config(fg=color, bg=color2)
    Count2_Label.config(fg=color, bg=color2)
    Answer1_Label.config(fg=color, bg=color2)
    Answer2_Label.config(fg=color, bg=color2)
    mainframe["bg"] = color2
    root.configure(bg=color2)

def convert_number(num):
    if num <= 9:
        num = f'0{num}'
    return num

# Adds event catchers for the buttons
GPIO.add_event_detect(L_Add, GPIO.RISING, callback=buttonPress, bouncetime=1000)
GPIO.add_event_detect(R_Add, GPIO.RISING, callback=buttonPress, bouncetime=1000)
GPIO.add_event_detect(L_Sub, GPIO.RISING, callback=buttonPress, bouncetime=1000)
GPIO.add_event_detect(R_Sub, GPIO.RISING, callback=buttonPress, bouncetime=1000)
GPIO.add_event_detect(Auto_Finish, GPIO.RISING, callback=buttonPress, bouncetime=3000)


# run(0, 0, mainframe)
root.mainloop()
GPIO.cleanup()

