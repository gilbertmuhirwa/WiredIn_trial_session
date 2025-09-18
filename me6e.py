import random
import math

# Data pairs: [normal_character, different_character]
data = [['O','0'], ['l','1'], ['m','n']]
number_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
level = 1
col = 5
row = 4

def start_message():
    print("Enter the cell number (e.g. A1) of the different character.")

def section_message():
    print("Level: " + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    mistake_number = random.randint(0, (col * row) - 1)
    print("Debug: mistake_number = " + str(mistake_number))
    question = data[choice_data]
    print(question)
    
    # Print column header
    question_str1 = '/|'
    question_str2 = '--'
    for i in range(col):
        question_str1 += number_data[i] + ' '
        question_str2 += '-'
    print(question_str1)
    print(question_str2)
    
    # Print grid
    for i in range(row):
        question_str = str(i + 1) + "|"
        for j in range(col):
            if (i * col + j) == mistake_number:
                question_str += question[1]  # Different character
            else:
                question_str += question[0]  # Normal character
        print(question_str)
    
    return mistake_number

def change_input_number(input_str):
    str_data = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}
    input_str_split = list(input_str.upper())
    col_number = str_data[input_str_split[0]]
    row_number = int(input_str_split[1]) - 1
    input_number = row_number * col + col_number
    return input_number

def is_correct_number(mistake_number, input_number):
    return mistake_number == input_number

def view_result(is_correct, mistake_number):
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect")
        print("The correct answer was " + change_string(mistake_number))

def change_string(number):
    col_number = number % col
    row_number = math.floor(number / col) + 1
    string = number_data[col_number] + str(row_number)
    return string

def play():
    section_message()
    mistake_number = view_question()
    choice = input("(E.g. A1) ")
    print("Debug: choice = " + choice)
    input_number = change_input_number(choice)
    print("Debug: input_number = " + str(input_number))
    is_correct = is_correct_number(mistake_number, input_number)
    view_result(is_correct, mistake_number)

# Run the game
start_message()
play()
