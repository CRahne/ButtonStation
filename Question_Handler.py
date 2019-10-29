# IMPORTS
import random


def Unpack_Questions():

    with open("Questions_converted.csv",'r') as Questions:
        Questions_list = []
        column = 0
        for value in Questions:
            column += 1
            Questions_list.append(value)

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

    return Questions

def getRandomQuestion():
    Questions = []
    Questions = Unpack_Questions()
    number = random.randint(0, 42)
    return Questions[number]

# q = Unpack_Questions()