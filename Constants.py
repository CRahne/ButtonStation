# Channel Numbers on PI for Buttons
L_Add = 23
R_Add = 25
L_Sub = 24
R_Sub = 18 
Auto_Finish = 4

# Sets the bouncetime for the buttons (The time before the program will register another press from that button, in milliseconds)
L_Add_Bouncetime = 1000
R_Add_Bouncetime = 1000
L_Sub_Bouncetime = 1000
R_Sub_Bouncetime = 1000
Auto_Finish_Bouncetime = 1000                                                                                                                                                                                       

# Tkinter Geometry Constants
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

# Answer 1
Answer1_Row = 1
Answer1_Column = 1
Answer1_padx = 0
Answer1_pady = 100
Answer1_Background = 'black'
Answer1_Font_Color = 'gold'
Answer1_Font = 'Consolas'
Answer1_Font_Size = 45

# Answer 2
Answer2_Row = 1
Answer2_Column = 3
Answer2_padx = 0
Answer2_pady = 100
Answer2_Background = 'black'
Answer2_Font_Color = 'gold'
Answer2_Font = 'Consolas'
Answer2_Font_Size = 45

# Count 1
Count1_Row = 2
Count1_Column = 1
Count1_padx = 0
Count1_pady = 100
Count1_Background = 'black'
Count1_Font_Color = 'gold'
Count1_Font = 'Hack'
Count1_Font_Size = 120

# Count 2
Count2_Row = 2
Count2_Column = 3
Count2_padx = 0
Count2_pady = 100
Count2_Background = 'black'
Count2_Font_Color = 'gold'
Count2_Font = 'Hack'
Count2_Font_Size = 120

# Question
Question_Row = 3
Question_Column = 1
Question_Columnspan = 3
Question_Background = 'black'
Question_Font_Color = 'gold'
Question_Font = 'Consolas'
Question_Font_Size = 60

# Image
# File Name For the Image. Must be .png
Photo_Image_File = "logo350.png"
Image_Row = 1
Image_Rowspan = 2
Image_Column = 2
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
Finish_Font_Color = 'black'
Finish_Background = 'gold'