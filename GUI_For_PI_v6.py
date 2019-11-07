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

# Sets the size and location of the window (In pixels)
root.geometry(f'{Constants.Window_Width}x{Constants.Window_Height}+{Constants.SpawnPoint_X}+{Constants.SpawnPoint_Y}')

# Root Background Colors
root.configure(bg=Constants.Window_Background_Color.lower())

# Creates Grid Object on the Window for placement
# of Labels
mainframe = Frame(root)
# Sets the background color of the frame
mainframe["bg"] = Constants.Window_Background_Color.lower()
# Sets up sticky so that it can be used when placing labels
mainframe.grid(sticky=(N, W, E, S))

# Sets up the columns
mainframe.columnconfigure(Constants.Window_Number_Of_Columns,
                          weight=Constants.Window_Column_Weight)

# Sets up the rows
mainframe.rowconfigure(Constants.Window_Number_Of_Rows,
                       weight=Constants.Window_Row_Weight)


# Gets a random question from file designated in Question_Handler.py
Start_Question = QH.getRandomQuestion()


###########
## Row 1 ##
###########

# Sets up the label and gets the string to be displayed
Answer_Left = StringVar()
Answer_Left.set(Start_Question[1])


# Applies the settings and displays the label
Answer_Left_Label = Label(mainframe,
                      textvariable=Answer_Left,
                      bg=Constants.Answer_Left_Background,
                      fg=Constants.Answer_Left_Font_Color,
                      font=f'{Constants.Answer_Left_Font} {Constants.Answer_Left_Font_Size} bold')

Answer_Left_Label.grid(row=Constants.Answer_Left_Row,
                   column=Constants.Answer_Left_Column,
                   padx=Constants.Answer_Left_padx,
                   pady=Constants.Answer_Left_pady)



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
Answer_Right = StringVar()
Answer_Right.set(Start_Question[2])


# Applies the settings and displays the label
Answer_Right_Label = Label(mainframe,
                      textvariable=Answer_Right,
                      bg=Constants.Answer_Right_Background,
                      fg=Constants.Answer_Right_Font_Color,
                      font=f'{Constants.Answer_Right_Font} {Constants.Answer_Right_Font_Size} bold')
Answer_Right_Label.grid(row=Constants.Answer_Right_Row,
                   column=Constants.Answer_Right_Column,
                   padx=Constants.Answer_Right_padx,
                   pady=Constants.Answer_Right_pady)



###########
## Row 2 ##
###########

# Sets up 1st Count Variable and Label
Count_Left = StringVar()
Count_Left.set('00')

Count_Left_Label = Label(mainframe,
                     textvariable=Count_Left,
                     bg=Constants.Count_Left_Background,
                     fg=Constants.Count_Left_Font_Color,
                     font=f'{Constants.Count_Left_Font} {Constants.Count_Left_Font_Size} bold')
Count_Left_Label.grid(row=Constants.Count_Left_Row,
                  column=Constants.Count_Left_Column,
                  padx=Constants.Count_Left_padx,
                  pady=Constants.Count_Left_pady)


# Sets up 2nd Count Variable and Label
Count_Right = StringVar()
Count_Right.set("00")

Count_Right_Label = Label(mainframe,
                     textvariable=Count_Right,
                     bg=Constants.Count_Right_Background,
                     fg=Constants.Count_Right_Font_Color,
                     font=f'{Constants.Count_Right_Font} {Constants.Count_Right_Font_Size} bold')
Count_Right_Label.grid(row=Constants.Count_Right_Row,
                  column=Constants.Count_Right_Column,
                  padx=Constants.Count_Right_padx,
                  pady=Constants.Count_Right_pady)



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
                    sticky=W+E+N+S) # Puts the question label in the middle of the grid space



# Runs whenever a button is pressed
def buttonPress(channel):
    
    # Accesses the randomly assigned Finish_Value
    global Finish_Value
    
    # If the counts are at the finish value
    if ((int(Count_Left.get()) == Finish_Value and channel == Constants.L_Add) or
       (int(Count_Right.get()) == Finish_Value and channel == Constants.R_Add)):
        finish(channel)
    
    # Adds One to Count_Left
    elif channel == Constants.L_Add:
        Count_Left.set(convert_number(int(Count_Left.get()) + 1))
    
    # Adds one to Count_Right
    elif channel == Constants.R_Add: 
        Count_Right.set(convert_number(int(Count_Right.get()) + 1))
    
    # Subtracts one from Count_Left
    elif (channel == Constants.L_Sub) and (int(Count_Left.get()) > 0):
        Count_Left.set(convert_number(int(Count_Left.get()) - 1))
    
    # Subtracts one from Count_Right
    elif(channel == Constants.R_Sub) and (int(Count_Right.get()) > 0):
        Count_Right.set(convert_number(int(Count_Right.get()) - 1))



# Runs when either Count is equal to Finish_Value or when the Auto_Finish button is pressed.
# Makes the screen flash, resets the numbers, and gets a new random question
def finish(channel):
    
    # Resets the values of both counts
    Count_Left.set('00')
    Count_Right.set('00')
    
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
    Answer_Left.set(New_Question[1])
    Answer_Right.set(New_Question[2])



# Changes the color of the text and background
def Flash(color_fg, color_bg):
    # Question
    Question_Label.config(fg=color_fg, bg=color_bg)
    
    # Counts
    Count_Left_Label.config(fg=color_fg, bg=color_bg)
    Count_Right_Label.config(fg=color_fg, bg=color_bg)
    
    # Answers
    Answer_Left_Label.config(fg=color_fg, bg=color_bg)
    Answer_Right_Label.config(fg=color_fg, bg=color_bg)
    
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
    Count_Left_Label.config(fg=Constants.Count_Left_Font_Color,
                        bg=Constants.Count_Left_Background)
    
    Count_Right_Label.config(fg=Constants.Count_Right_Font_Color,
                        bg=Constants.Count_Right_Background)
    
    #Answer Labels
    Answer_Left_Label.config(fg=Constants.Answer_Left_Font_Color,
                         bg=Constants.Answer_Left_Background)
    
    Answer_Right_Label.config(fg=Constants.Answer_Right_Font_Color,
                         bg=Constants.Answer_Right_Background)
    
    
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



# Sets up a loop to update the GUI
root.mainloop()