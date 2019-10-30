# QUICK FIXES

If you are having problems, you can take a look in here and see if there are any solutions. These are only possibilities and are not the definite answer for all cases.

## Question_Handler.py

### Illegal Character

Something to do with how windows encodes something. Just need to open it in a text editor and copy and paste the csv file values into new csv file.

### Wrong File

Go to where it says 'with(open' in the Unpack_Questions() function. Then change the file that it is opening

### Incorrect Formatting

1) Check to make sure you have a comma at the end of all of the lines in the csv
2) Check to make sure you have only 3 values of information stored on each line
3) Question Conversion could potentially be wrong

## ButtonFactory/Button Setup

### Correct Channels Aren't Working

Check to where you set the mode of the GPIO to either BCM or BOARD (this changes how the channels are referenced)

### Button Inputs Aren't Registering

1) Are channels correct?
2) Is the wiring set up correctly?
3) Does the button setup settings work with how the wiring is (see GPIO.setup in ButtonFactory Class)

### Buttons are Phantom Pressing

Sometimes with limit switches, they are touchy. So they will register hits when it you don't press it
