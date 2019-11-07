# Change Values in here are called in the main file,
# GUI_For_PI_v6.py. By using this file, you can change
# everything in one places.

# Channel Numbers on PI for Buttons
L_Add = 23      # Adds One to the Left Count
R_Add = 25      # Adds One to the Right Count
L_Sub = 24      # Subtracts One from the Left Count
R_Sub = 18      # Subtracts One from the Right Count
Auto_Finish = 4 # Resets the Poll

# Sets the bouncetime for the buttons (The time before the program will register another press from that button, in milliseconds)
L_Add_Bouncetime = 1000
R_Add_Bouncetime = 1000
L_Sub_Bouncetime = 1000
R_Sub_Bouncetime = 1000
Auto_Finish_Bouncetime = 3000                                                                                                                                                                                       

# Tkinter Geometry Configurations
 # Spawnpoints are where the GUI pops up when initialized. They
 # should always be set to 0 (upper left-hand corner)
SpawnPoint_X = 0
SpawnPoint_Y = 0
 # These control the size of the window. If you want full screen,
 # just use the pixel dimensions of the moniter that you are using
Window_Width = 1600
Window_Height = 900

# Window Variables
Window_Background_Color = 'black'
Window_Number_Of_Columns = 3
Window_Column_Weight = 100
Window_Number_Of_Rows = 3
Window_Row_Weight = 100

# Answer Left
# Location of the label in the grid
Answer_Left_Row = 1
Answer_Left_Column = 1
# Adds spacing
Answer_Left_padx = 0
Answer_Left_pady = 100
# Label colors
Answer_Left_Background = 'black'
Answer_Left_Font_Color = 'gold'
# Font settings
Answer_Left_Font = 'Consolas' # Any font can be used as long as it is installed
Answer_Left_Font_Size = 45

# Answer Right
# Location of the label in the grid
Answer_Right_Row = 1
Answer_Right_Column = 3
# Adds spacing
Answer_Right_padx = 0
Answer_Right_pady = 100
Answer_Right_Background = 'black'
Answer_Right_Font_Color = 'gold'
# Font settings
Answer_Right_Font = 'Consolas' # Any font can be used as long as it is installed
Answer_Right_Font_Size = 45

# Count Left
# Location of the label in the grid
Count_Left_Row = 2
Count_Left_Column = 1
# Adds spacing
Count_Left_padx = 0
Count_Left_pady = 100
Count_Left_Background = 'black'
Count_Left_Font_Color = 'gold'
# Font settings
Count_Left_Font = 'Hack' # Any font can be used as long as it is installed
Count_Left_Font_Size = 120

# Count Right
# Location of the label in the grid
Count_Right_Row = 2
Count_Right_Column = 3
# Adds spacing
Count_Right_padx = 0
Count_Right_pady = 100
Count_Right_Background = 'black'
Count_Right_Font_Color = 'gold'
# Font settings
Count_Right_Font = 'Hack' # Any font can be used as long as it is installed
Count_Right_Font_Size = 120

# Question (This label uses sticky to stay centered instead of padding)
# Location of the label in the grid
Question_Row = 3
Question_Column = 1
Question_Columnspan = 3 # Allows the label to span 3 columns
Question_Background = 'black'
Question_Font_Color = 'gold'
# Font settings
Question_Font = 'Consolas' # Any font can be used as long as it is installed
Question_Font_Size = 60

# Image
# File Name For the Image. Must be .png
Photo_Image_File = "logo350.png"
# Location of the image in the grid
Image_Row = 1
Image_Rowspan = 2 # Allows the image to span 2 rows
Image_Column = 2
# Adds spacing
Image_padx = 80
Image_pady = 0
Image_Background = 'black'

# Finish Settings
# Limits for generating a random number for the Finish_Value
# random.randint(Finish_Value_Lower_Limit, Finish_Value_Upper_Limit)
Finish_Value_Upper_Limit = 25
Finish_Value_Lower_Limit = 5
# Time inbetween screen changes, in seconds
Finish_Flash_Time = 0.5
Finish_Flash_Font_Color = 'black'
Finish_Flash_Background_Color = 'gold'