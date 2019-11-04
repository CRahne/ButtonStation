# Intro_CS_GUI
This program is designed to run on a raspberry pi.

This is designed to work with a five button interface. One button to reset the program, two buttons
to add and subtract from the left value, and two buttons to add and subtract from the right value.

The program will select a random "This or That" style question and display it. Users' responses to the
question will be kept track of using two counts. The counts will be added to or subracted from whenever
a user presses a button. The program will choose a random number between two preset values, and once 
either of the counts reaches that number, the screen will briefly flash, then reset the counts and 
choose a different random question.

In order to run the program, run GUI_For_PI_v6.py.

# Wiring
![alt text](https://github.com/CRahne/Intro_CS_GUI/blob/Library/Docs/Diagram.jpg)
Our wiring was done on a 40-pin pi, and the default pins are 4, 18, 23, 24, and 25.

# Files
### ButtonFactory.py
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
If you want to create a new file containing questions, it must be in .csv format and located in the same folder as Question_Handler.py.
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
file. The resolution size of the image should be smaller than the size of the window, and you may have to adjust padx and pady variables in Constants.py in order to make the image look natural.

# Adding and Removing Buttons
In order to add or remove buttons, open GUI_For_PI_v6.py. In order to remove a button, remove the ButtonFactory class call
of the button you wish to remove. You may also remove the variables containing the settings for that button if you wish(They will
be located in Constants.py). If you wish to add a button, Then add a ButtonFactory call in GUI_For_PI_v6.py. This class takes three parameters: The pin number of the button, the method to be called when the button is pressed, and the bouncetime of the button in milliseconds. For example, if you wanted to add a button on pin 5 that called the buttonPress function when pressed and had a bouncetime of 1 second, your code should look like this:

`ButtonFactory(5, buttonPress, 1000)`

# Changing other Settings
All other settings will be changed using the variables in Constants.py.

### Changing the screen resolution / window size
The settings for the size of the window are near the top of Constants.py. Changing these numbers will change the size of the 
window, but font size, the size of the image, and padding **will not** adjust to fit the new settings, and will have to be
adjusted manually using the padx, pady, and font size variables in Constants.py

