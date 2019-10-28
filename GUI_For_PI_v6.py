from tkinter import *
import time
import random
import RPi.GPIO as GPIO
import Question_Handler as QH
from Button_Object import Button_Object
import Constants

# Sets up GPIO for channel reference. For BOARD vs BCM, Look Here:
# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)

# Gets a number 5 through 25 that will determine when the program will restart
Finish_Value = random.randint(Constants.Finish_Value_Lower_Limit, Constants.Finish_Value_Upper_Limit)
 
root = Tk()
root.geometry(f'{Constants.Window_Width}x{Constants.Window_Height}+{Constants.SpawnPoint_X}+{Constants.SpawnPoint_Y}')
root.configure(bg=Constants.Window_Background_Color.lower())

PHOTO = PhotoImage(file=Constants.Photo_Image_File)

mainframe = Frame(root)
mainframe["bg"] = Constants.Window_Background_Color.lower()
mainframe.grid(column=Constants.Window_Number_Of_Columns, row=Constants.Window_Number_Of_Rows, sticky=(N, W, E, S))

# Sets up the rows and columns of the grids
mainframe.columnconfigure(3, weight=100)
mainframe.rowconfigure(3, weight=100)

# Settings for the image
Image_padx = 80
Image_pady = 0

# Settings for the answer labels
Answer_Label_pady = 100
Answer_Label_padx = 0
Answer_Label_Font = 'Consolas'
Answer_Label_Fontsize = 45

# Settings for the numbers
Number_pady = 100
Number_padx = 0
Number_Font = 'Hack'
Number_Fontsize = 120

# Settings for the question
Question_Font = 'Consolas'
Question_Fontsize = 60

# Row 1

# Gets a random question from Question_Handler.py (Imported at the top as QH)
Start_Question = QH.getRandomQuestion()

# Sets up the label and gets the string to be displayed
Answer1 = StringVar()
Answer1.set(Start_Question[1])

# Applies the settings and displays the label
Answer1_Label = Label(mainframe, textvariable=Answer1, bg='black', fg='gold', font=f'{Answer_Label_Font} {Answer_Label_Fontsize} bold')
Answer1_Label.grid(row=1, column=1, padx=Answer_Label_padx, pady=Answer_Label_pady)

# Sets up the image settings and displays the image
photo_label = Label(mainframe, image=PHOTO, bg='black')
photo_label.grid(row=1, rowspan = 2, column = 2, sticky = W+E+N+S, padx = Image_padx)

# Sets up the label and gets the string to be displayed
Answer2 = StringVar()
Answer2.set(Start_Question[2])

# Applies the settings and displays the label
Answer2_Label = Label(mainframe,textvariable=Answer2,bg='black',fg='gold', font=f'{Answer_Label_Font} {Answer_Label_Fontsize} bold')
Answer2_Label.grid(row=1,column=3, padx=Answer_Label_padx, pady=Answer_Label_pady)

# Row 2

# Sets up the label
Count1 = StringVar()
Count1.set('00')

# Applies the settings and displays the number
Count1_Label = Label(mainframe, textvariable=Count1, bg='black', fg='gold', font=f'{Number_Font} {Number_Fontsize} bold')
Count1_Label.grid(row=2, column=1, padx=Number_padx, pady=Number_pady)

# Sets up the label
Count2 = StringVar()
Count2.set("00")

# Applies the settings and displays the number
Count2_Label = Label(mainframe,textvariable=Count2,bg='black',fg='gold', font=f'{Number_Font} {Number_Fontsize} bold')
Count2_Label.grid(row=2,column=3,padx=Number_padx, pady=Number_pady)

# Row 3

# Gets the the question and sets up the label
Question = StringVar()
Question.set(Start_Question[0])

# Applies the settings and displays the question
Question_Label = Label(mainframe,textvariable=Question,bg='black',fg='gold', font=f'{Question_Font} {Question_Fontsize} bold')
Question_Label.grid(row=3, column=1, columnspan = 3, sticky=W+E+N+S) #padx=padx_Size, pady=pady_Size

# Runs whenever a button is pressed
def buttonPress(channel):
    
    global Finish_Value
    
    if (int(Count1.get()) == Finish_Value and channel == Constants.L_Add) or (int(Count2.get()) == Finish_Value and channel == R_Add):
        finish(channel)
    
    elif channel == Constants.L_Add:
        Count1.set(convert_number(int(Count1.get()) + 1))
        
    elif channel == Constants.R_Add: # Adds 1 to Count2
        Count2.set(convert_number(int(Count2.get()) + 1))
    
    elif (channel == Constants.L_Sub) and (int(Count1.get()) > 0):
        Count1.set(convert_number(int(Count1.get()) - 1))
    
    elif(channel == Constants.R_Sub) and (int(Count2.get()) > 0):
        Count2.set(convert_number(int(Count2.get()) - 1))

# Runs when either Count is equal to Finish_Value or when the Auto_Finish button is pressed.
# Makes the screen flash, resets the numbers, and gets a new random question
def finish(channel):
    # Resets the values
    Count1.set('00')
    Count2.set('00')
    # Makes the screen flash twice
    for x in range(2):
        change_color('black','gold')
        time.sleep(0.5)    
        change_color('gold','black')
        time.sleep(0.5)
    
    # Gets another random number between 5 and 25 to determine when the program will restart
    Finish_Value = random.randint(Constants.Finish_Value_Lower_Limit, Constants.Finish_Value_Upper_Limit)
    
    # Gets a new random question
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

# Adds a 0 to the beginning of the number if it is a single digit number(ex. 1 = 01)
def convert_number(num):
    if num <= 9:
        num = f'0{num}'
    return num


L_Add_Button = Button_Object(Constants.L_Add, buttonPress, 1000)
R_Add_Button = Button_Object(Constants.R_Add, buttonPress, 1000)
L_Sub_Button = Button_Object(Constants.L_Sub, buttonPress, 1000)
R_Sub_Button = Button_Object(Constants.R_Sub, buttonPress, 1000)
Auto_Finish = Button_Object(Constants.Auto_Finish, finish, 1000)


# Updates the screen
root.mainloop()