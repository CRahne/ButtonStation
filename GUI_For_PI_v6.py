# IMPORTS

 # Standard Library
from tkinter import *                    # GUI Framework
import time                              # For time.sleep()
import random                            # Random Numbers
import RPi.GPIO as GPIO                  # Allows us to interact with Raspberry PI GPIO

 # Custom
import Question_Handler as QH            # Gets the Questions from Questions_converted.csv
from ButtonFactory import ButtonFactory  # A class that will set up the buttons
import Constants                         # Constant Values that will be called in the program


# Gets the random stop value for the first iteration of the program
Finish_Value = random.randint(Constants.Finish_Value_Lower_Limit,
                              Constants.Finish_Value_Upper_Limit)
 

# Creates Root Window Object for the GUI
root = Tk()

# Root Size and Placement
root.geometry(f'{Constants.Window_Width}x{Constants.Window_Height}+{Constants.SpawnPoint_X}+{Constants.SpawnPoint_Y}')

# Root Background Colors
root.configure(bg=Constants.Window_Background_Color.lower())

# Creates Grid Object on the Window for placement
# of Labels
mainframe = Frame(root)
mainframe["bg"] = Constants.Window_Background_Color.lower()
mainframe.grid(sticky=(N, W, E, S))

mainframe.columnconfigure(Constants.Window_Number_Of_Columns,
                          weight=Constants.Window_Column_Weight)

mainframe.rowconfigure(Constants.Window_Number_Of_Rows,
                       weight=Constants.Window_Row_Weight)



###########
## Row 1 ##
###########

# Gets a random question from fiel deswignated in
# Question_Handler.py
Start_Question = QH.getRandomQuestion()

# Sets up the label and gets the string to be displayed
Answer1 = StringVar()
Answer1.set(Start_Question[1])

# Applies the settings and displays the label
Answer1_Label = Label(mainframe,
                      textvariable=Answer1,
                      bg=Constants.Answer1_Background,
                      fg=Constants.Answer1_Font_Color,
                      font=f'{Constants.Answer1_Font} {Constants.Answer1_Font_Size} bold')

Answer1_Label.grid(row=Constants.Answer1_Row,
                   column=Constants.Answer1_Column,
                   padx=Constants.Answer1_padx,
                   pady=Constants.Answer1_pady)


# Sets up the image settings and displays the image
PHOTO = PhotoImage(file=Constants.Photo_Image_File)

photo_label = Label(mainframe,
                    image=PHOTO,
                    bg=Constants.Image_Background)
photo_label.grid(row=Constants.Image_Row,
                 rowspan = Constants.Image_Rowspan,
                 column = Constants.Image_Column,
                 sticky = W+E+N+S,
                 padx = Constants.Image_padx,
                 pady=Constants.Image_pady)


# Sets up the label and gets the string to be displayed
Answer2 = StringVar()
Answer2.set(Start_Question[2])

# Applies the settings and displays the label
Answer2_Label = Label(mainframe,
                      textvariable=Answer2,
                      bg=Constants.Answer2_Background,
                      fg=Constants.Answer2_Font_Color,
                      font=f'{Constants.Answer2_Font} {Constants.Answer2_Font_Size} bold')
Answer2_Label.grid(row=Constants.Answer2_Row,
                   column=Constants.Answer2_Column,
                   padx=Constants.Answer2_padx,
                   pady=Constants.Answer2_pady)



###########
## Row 2 ##
###########

# Sets up 1st Count Variable and Label
Count1 = StringVar()
Count1.set('00')

Count1_Label = Label(mainframe,
                     textvariable=Count1,
                     bg=Constants.Count1_Background,
                     fg=Constants.Count1_Font_Color,
                     font=f'{Constants.Count1_Font} {Constants.Count1_Font_Size} bold')
Count1_Label.grid(row=Constants.Count1_Row,
                  column=Constants.Count1_Column,
                  padx=Constants.Count1_padx,
                  pady=Constants.Count1_pady)

# Sets up 2nd Count Variable and Label
Count2 = StringVar()
Count2.set("00")

Count2_Label = Label(mainframe,
                     textvariable=Count2,
                     bg=Constants.Count2_Background,
                     fg=Constants.Count2_Font_Color,
                     font=f'{Constants.Count2_Font} {Constants.Count2_Font_Size} bold')
Count2_Label.grid(row=Constants.Count2_Row,
                  column=Constants.Count2_Column,
                  padx=Constants.Count2_padx,
                  pady=Constants.Count2_pady)



###########
## Row 3 ##
###########

# Sets Up Question Label and Variable
Question = StringVar()
Question.set(Start_Question[0])

Question_Label = Label(mainframe,
                       textvariable=Question,
                       bg=Constants.Question_Background,
                       fg=Constants.Question_Font_Color,
                       font=f'{Constants.Question_Font} {Constants.Question_Font_Size} bold')
Question_Label.grid(row=Constants.Question_Row,
                    column=Constants.Question_Column,
                    columnspan = Constants.Question_Columnspan,
                    sticky=W+E+N+S)



# Runs whenever a button is pressed
def buttonPress(channel):
    
    global Finish_Value
    
    if ((int(Count1.get()) == Finish_Value and channel == Constants.L_Add) or
       (int(Count2.get()) == Finish_Value and channel == Constants.R_Add)):
        finish(channel)
    
    elif channel == Constants.L_Add:
        Count1.set(convert_number(int(Count1.get()) + 1))
        
    elif channel == Constants.R_Add: 
        Count2.set(convert_number(int(Count2.get()) + 1))
    
    elif (channel == Constants.L_Sub) and (int(Count1.get()) > 0):
        Count1.set(convert_number(int(Count1.get()) - 1))
    
    elif(channel == Constants.R_Sub) and (int(Count2.get()) > 0):
        Count2.set(convert_number(int(Count2.get()) - 1))



# Runs when either Count is equal to Finish_Value or when the Auto_Finish button is pressed.
# Makes the screen flash, resets the numbers, and gets a new random question
def finish(channel):
    
    # Resets the values of both counts
    Count1.set('00')
    Count2.set('00')
    
    # Makes the screen flash twice using a for loop counter
    for x in range(2):
        Flash(Constants.Finish_Flash_Font_Color,
              Constants.Finish_Flash_Background_Color)
    
    # Gets another random number between 5 and 25 to
    # determine when the program will restart the next
    # iteration
    Finish_Value = random.randint(Constants.Finish_Value_Lower_Limit,
                                  Constants.Finish_Value_Upper_Limit)
    
    # Gets and then displays a new question
    New_Question = QH.getRandomQuestion()
    Question.set(New_Question[0])
    Answer1.set(New_Question[1])
    Answer2.set(New_Question[2])



# Changes the color of the text and background
def Flash(color_fg, color_bg):
    # Question
    Question_Label.config(fg=color_fg, bg=color_bg)
    
    # Counts
    Count1_Label.config(fg=color_fg, bg=color_bg)
    Count2_Label.config(fg=color_fg, bg=color_bg)
    
    # Answers
    Answer1_Label.config(fg=color_fg, bg=color_bg)
    Answer2_Label.config(fg=color_fg, bg=color_bg)
    
    # Photo
    photo_label.config(bg=color_bg)
    
    # Window
    mainframe["bg"] = color_bg
    root.configure(bg=color_bg)
    
    # Will stop for a bit and then turn back.
    time.sleep(Constants.Finish_Flash_Time)    
    Revert_Colors()
    time.sleep(Constants.Finish_Flash_Time)



# This changes the colors back on the screen to the original
# colors.
def Revert_Colors():
    
    # Question Label
    Question_Label.config(fg=Constants.Question_Font_Color,
                          bg=Constants.Question_Background)
    
    # Count Labels
    Count1_Label.config(fg=Constants.Count1_Font_Color,
                        bg=Constants.Count1_Background)
    
    Count2_Label.config(fg=Constants.Count2_Font_Color,
                        bg=Constants.Count2_Background)
    
    #Answer Labels
    Answer1_Label.config(fg=Constants.Answer1_Font_Color,
                         bg=Constants.Answer1_Background)
    
    Answer2_Label.config(fg=Constants.Answer2_Font_Color,
                         bg=Constants.Answer2_Background)
    
    
    # Photo Label
    photo_label.config(bg=Constants.Image_Background)
    
    
    # Window Backgrounds
    mainframe["bg"] = Constants.Window_Background_Color
    root.configure(bg=Constants.Window_Background_Color)



# Will take the parameter num and if it is only one digit,
# the program will add a zero in front of it. It will return
# the value as a string
def convert_number(num):
    if num <= 9:
        return f'0{num}'
    return str(num)



# Sets up GPIO for channel reference. For BOARD vs BCM, Look Here:
# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)



# Sets Up Buttons with the ButtonFactory Class in
# ButtonFactory.py. This will use values from
# Constants.py

ButtonFactory(Constants.L_Add, buttonPress,           # Left Adding Button
              Constants.L_Add_Bouncetime)
 
ButtonFactory(Constants.R_Add, buttonPress,           # Right Adding Button
              Constants.R_Add_Bouncetime)

ButtonFactory(Constants.L_Sub, buttonPress,           # Left Subtraction Button
              Constants.L_Sub_Bouncetime)

ButtonFactory(Constants.R_Sub, buttonPress,           # Right Subtraction Button
              Constants.R_Sub_Bouncetime)

ButtonFactory(Constants.Auto_Finish, finish,          # Auto-Finish Button
              Constants.Auto_Finish_Bouncetime)



# Runs GUI
root.mainloop()