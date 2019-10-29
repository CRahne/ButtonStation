# IMPORTS
import random

# Takes the raw values from a csv file and then
# will seperate them into a 2D array spit up by
# line.
def Unpack_Questions():
    
    # Opens and gets the raw values
    with open("Questions_converted.csv",'r') as Questions:
        Questions_list = []
        column = 0
        for value in Questions:
            column += 1
            Questions_list.append(value)

    # Converts and sepeartes the values
    string_holder = []
    Questions_holder = []
    Questions = []

    for stock in Questions_list:
        holding_list = list(stock)
        for char in holding_list:
            if char == ",":
                Questions_holder.append(''.join(string_holder))
                string_holder.clear()
                if len(Questions_holder) == 3:
                    Questions.append(Questions_holder)
                    Questions_holder = []
            elif char == "\n":
                pass
            else:
                string_holder.append(char)
    
    # Returns the 2D Array
    return Questions

# Will return an 1D array of the question, answer1, answer2
# that was randomaly picked.
def getRandomQuestion():
    Questions = []
    Questions = Unpack_Questions()
    number = random.randint(0, (len(Questions)-1)) # Avoids index error
    return Questions[number]