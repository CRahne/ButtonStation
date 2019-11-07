# ButtonStation

A GUI that will act as a scoreboard for a this or that questionnaire. It will be controlled by 5 buttons that are hooked up to a raspberry pi. The program will also pick a random end point and then resets itself with a new question.

---

## Set Up and Installation

### Software

1) `git clone https://github.com/CRahne/ButtonStation.git` into a desired directory on the PI.
2) You can tweak parts of the program in Constants.py or Questions.csv (more on that later)
3) [Install Python 3](https://www.python.org/downloads/). This will install the tkinter module, the used GUI framework.
3) Run [ButtonStation_v6.py](ButtonStation_v6.py), which is in the root directory

### Wiring
![alt text](Docs/Diagram.jpg)
This is a diagram for the Raspberry PI model 4 with a 40 pin layout. You will also need to give it a power supply, a hdmi output, and connections to a USB mouse and keyboard.

---

## Configuration

### GUI (Window) Size

The settings for the size of the window are near the top of Constants.py. Changing these numbers will change the size of the 
window, but font size, the size of the image, and padding **will not** adjust to fit the new settings, and will have to be
adjusted manually using the padx, pady, and font size variables in Constants.py. To go full screen, get your monitor pixel dimensions/resolution.

### Questions

1) Change or Add questions in the Questions.csv file. An example would be, ```Favorite Animal?, Cat, Dog,```. Note the final comma at the end of the line, as that is important in the next step. Also, if you wanted different sets of questions, you can have multiple csv files.
2) Run [Question_Converter.py](Question_Converter.py). It will prompt for the filename that stores your questions in [Questions_converted.csv](Questions_converted.csv).
3) Change the GUI Constraints in [Constants.py](Constants.py).

### Center Photo

You will need to place the desired photo (which must be .png) into the root directory. Then, you must change the ```Photo_Image_File``` variable in [Constants.py](Constants.py). You may need to adjust other variables, such as padding, to account for the size of the photo.

### Changing Button GPIO Pins

The default pins of the buttons are stored in [Constants.py](Constants.py). They are as follows:

```python
L_Add = 23      # Adds One to the Left Count
R_Add = 25      # Adds One to the Right Count
L_Sub = 24      # Subtracts One from the Left Count
R_Sub = 18      # Subtracts One from the Right Count
Auto_Finish = 4 # Resets the Poll
```

To edit these, you simply need to change the value assigned to the variable.

### Colors

There are many variables in [Constants.py](Constants.py) that relate to this.



---

## Files

### Directory Overview
```
.
+-- BackUpImages
|   +-- Logo.png
|   +-- logo300.png
|   +-- logo325.png
|   +-- logo400.png
|
+-- Docs
|   +-- Diagram.jpg
|   +-- FIXME.md
|
+-- OldVersions
|   +-- ButtonStation_v1.py
|   +-- ButtonStation_v2.py
|   +-- ButtonStation_v3.py
|   +-- ButtonStation_v4.py
|   +-- ButtonStation_v5.py
|
+-- TestScripts
|   +-- ButtonTester.py
|   +-- ButtonTester_With_Events.py
|   +-- Test_GUI.py
|
+-- ButtonFactory.py
+-- Constants.py
+-- ButtonStation_v6.py
+-- logo350.png
+-- Question_Handler.py
+-- Questions.csv
+-- Questions_converted.csv
+-- README.md
```

### [ButtonFactory.py](ButtonFactory.py)
This file is used to set up the buttons and adds event catchers for each button.

### [Constants.py](Constants.py)
This file stores most of the variables used by the program. This keeps most of the values in one spot, making 
customizing the program much easier.

### [ButtonStation_v6.py](ButtonStation_v6.py)
This is where the majority of the logic takes place. All GUI setup, updates, and general control is done here.

### [Question_Handler.py](Question_Handler.py)
This program formats the questions into a form that can be displayed in the GUI. It returns a random question
and it's two responses.

### [Questions.csv](Questions.csv)
This is where all of the pre-converted questions are stored. This file is never directly interfaced with by the
program, and exists only for the programmer to interact with when adding or removing questions.

### [Questions_converted.csv](Questions_converted.csv)
This file stores all of the converted questions. This is the file that is referenced by the program when getting
a random question.

### [logo350.png](logo350.png)
This is the default image to be displayed by the program.

### [Question_Converter.py](Question_Converter.py)
This program converts the questions in Questions.csv and stores the new questions in Questions_converted.csv. It
is only used by the programmer when adding or removing questions.

---

## Others

### Adding or Removing Questions

#### Adding a Question
In order to add a question, you must go to Questions.csv and add the question and it's two respsonses. Each entry
must be comma seperated. Each line should look like this:
`Question,Response,Response,`
If you want to create a new file containing questions, it must be in .csv format and located in the same folder as Question_Handler.py.
After you have added the questions you want to add, you must run Question_Converter.py. When prompted, input the
name of the file containing the new questions, and enter "y" when prompted to write the converted questions to 
Questions.converted.csv.

#### Removing a Question
Open Questions.csv and delete the line containing the question you wish to remove. Open Questions_converted.csv and
delete the question you wish to remove. You must delete the question from Questions.csv **_and_** Questions_converted.csv
in order to permanently remove a question.

# Adding and Removing Buttons
In order to add or remove buttons, open ButtonStation_v6.py. In order to remove a button, remove the ButtonFactory class call
of the button you wish to remove. You may also remove the variables containing the settings for that button if you wish(They will
be located in Constants.py). If you wish to add a button, Then add a ButtonFactory call in ButtonStation_v6.py. This class takes three parameters: The pin number of the button, the method to be called when the button is pressed, and the bouncetime of the button in milliseconds. For example, if you wanted to add a button on pin 5 that called the buttonPress function when pressed and had a bouncetime of 1 second, your code should look like this:

`ButtonFactory(5, buttonPress, 1000)`

