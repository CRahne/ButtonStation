# Intro_CS_GUI
This program is designed to run on a raspberry pi.

This is designed to work with a five button interface. One button to reset the program, two buttons
to add and subtract from the left value, and two buttons to add and subtract from the right value.

The program will select a random "This or That" style question and display it. Users' responses to the
question will be kept track of using two counts. The counts will be added to or subracted from whenever
a user presses a button. The program will choose a random number between two preset values, and once 
either of the counts reaches that number, the screen will briefly flash, then reset the counts and 
choose a different random question.

# Files
### Button_Object.py
This file is used to set up the buttons and adds event catchers for each button.

### Constants.py
This file stores most of the variables used by the program. This keeps most of the values in one spot, making 
customizing the program much easier.

### GUI_For_PI_v6.py
This is where the majority of the logic takes place. All GUI setup, updates, and general control is done here.

### Question_Handler.py
This program formats the questions into a form that can be displayed in the GUI. It returns a random question
and it's two responses.

### Questions.csv
This is where all of the pre-converted questions are stored. This file is never directly interfaced with by the
program, and exists only for the programmer to interact with when adding or removing questions.

### Questions_converted.csv
This file stores all of the converted questions. This is the file that is referenced by the program when getting
a random question.

### logo350.png
This is the default image to be displayed by the program.

### Question_Converter.py
This program converts the questions in Questions.csv and stores the new questions in Questions_converted.csv. It
is only used by the programmer when adding or removing questions.

# Adding or Removing Questions

### Adding a Question
In order to add a question, you must go to Questions.csv and add the question and it's two respsonses. Each entry
must be comma seperated. Each line should look like this:
`Question,Response,Response,`
After you have added the questions you want to add, you must run Question_Converter.py. When prompted, input the
name of the file containing the new questions, and enter "y" when prompted to write the converted questions to 
Questions.converted.csv.

### Removing a Question
Open Questions.csv and delete the line containing the question you wish to remove. Open Questions_converted.csv and
delete the question you wish to remove. You must delete the question from Questions.csv **_and_** Questions_converted.csv
in order to permanently remove a question.

# Changing the Image
In order to change the image, you must place the new image file into the folder with the rest of the files. The new
image must be in .png format. Then, open Constants.py and change the Photo_Image_File variable to the name of the new image
file.

# Changing other Settings
If you need to change the button pins, background or font colors, or other program settings, open the Constants.py file and
find the variables that correspond to the value you wish to change. If you change resolution settings (Window height and width),
you will also have to change padx and pady settings in order to make the display look natural.
