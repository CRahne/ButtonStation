# This script will take all of the values in a csv (comma seperated value file) and update
# the [1] and [2] values on each line to be the same length as the longest value. It will fill
# it in with spaces on both sides. This means that the questions should be stored like this
# in a csv file:
#
# Question,Answer1,Answer2,
#
# Note the comma after Answer2. That is important to the function of this program.
# This is what is used to make Questions_converted.csv


# User Inputs filename
filename = input("CSV File Name (without extension): ")

# Opening and getting the values in the selected file
with open(f"{filename}.csv",'r') as File:
    print("\nGetting Raw Values . . . . ")
    Questions_list = []
    column = 0
    for value in File:
        column += 1
        Questions_list.append(value)

string_holder = []
Questions_holder = []
Questions = []

# Formats into a 2D array, seperated by lines and commas
for question in Questions_list:
    holding_list = list(question)
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

# Gets greatest length
greatest_length = 0
for question in Questions:
    if len(str(question[1])) > greatest_length:
        greatest_length = len(str(question[1]))
    if len(str(question[2])) > greatest_length:
        greatest_length = len(str(question[2]))
print("The greatest char amount is " + str(greatest_length))
print("Converting . . . . \n")
 
 # Actual Conversion
for question in Questions:
    answers = [question[1], question[2]]
    x = 1
    for answer in answers:
        length = len(answer)
        needed_length = (greatest_length - length) / 2
        if length < greatest_length:
            if (needed_length % 1) != 0:
                parts = [" " * int(needed_length - 0.5), answer, " " * int(needed_length + 0.5)]
            else:
                parts = [" " * int(needed_length), answer, " " * int(needed_length)]
        else:
            parts = [answer]
        holder = ''.join(parts)
        if x == 1:
            question[1] = str(holder)
            x = 2
        else:
            question[2] = str(holder)
            x = 1
#             print(question[1]," | ",question[2]) # Uncomment if you want to see all of the values previously

# If the program messed up and didn't do what it was suppose to do,
# this code will check if the values are all the same length. If they aren't
# then the code will raise an error
isbad = False
for x in Questions:
    if len(x[2]) != greatest_length or  len(x[1]) != greatest_length:
        print("ERROR:")
        print(len(x[1]),'  || 1 ||  ', x[1])
        print(len(x[2]),'  || 2 ||  ', x[2])
        isbad = True
if isbad:
    int('a')
        
# If the user wants to keep the values, it will write them to a new file
# called filename_converted
choice = input("Do you want to write to a file? y/n  ")
if choice.upper() == "Y":
    with open(f'Questions_converted.csv','w+') as file:
        Amount_Of_Questions = len(Questions)
        Question_Ticker = 1
        for Question in Questions:
            if Question_Ticker != Amount_Of_Questions:
                appending_string = ','.join(Question)  + ',\n'
                Question_Ticker += 1
            else:
                appending_string = ','.join(Question)  + ','
            file.write(appending_string)        