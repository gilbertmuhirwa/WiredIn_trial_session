import math

# Fixed character pair and grid settings
# Each sublist contains [main character, odd one out]
data = [['l', '1'], ['O', '0'], ['m', 'n']] 
level = 1  # Game level
col = 5    # Number of columns in the grid
row = 4    # Number of rows in the grid
number_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']  # Column labels

# Display the starting message for the player
def start_message():
    print("Input cell number (e.g., A1) of different character.")

# Display the current level
def section_message():
    print("Level: " + str(level))

# Display the grid with the odd character in a fixed location
def view_question():
    choice_data = 1       # Fixed choice to select ['O','0']
    mistake_number = 8    # Fixed cell index of the odd character
    print("Debug: mistake_number = " + str(mistake_number))

    question = data[choice_data]  # Get the character pair
    print(question)                # Show the chosen character pair

    # Generate and print column headers
    header_row = "/|" + "".join(number_data[:col])
    separator_row = "-" * len(header_row)
    print(header_row)
    print(separator_row)

    # Generate and print each row of the grid
    for i in range(row):
        row_str = str(i+1) + "|"   # Row number
        for j in range(col):
            cell_index = i * col + j  
            # Explanation: cell_index = linear index of the grid
            # e.g., for i=1, j=3, cell_index = 1*5 + 3 = 8 (second row, 4th column)
            if cell_index == mistake_number:
                row_str += question[1]  # Place the odd character
            else:
                row_str += question[0]  # Place the main character
        print(row_str)

    return mistake_number, question  # Return the odd character's position

# Convert player input (e.g., 'A1') to a numeric index in the grid
def change_input_number(input_str):
    str_data = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }
    col_number = str_data[input_str[0].upper()]  # Convert column letter to index
    row_number = int(input_str[1]) - 1           # Convert row number to zero-based index
    input_number = row_number * col + col_number # Convert 2D grid to linear index
    # Inline explanation: linear index = row_index * number_of_columns + col_index
    # Example: D2 -> col_index=3, row_index=1 -> 1*5 + 3 = 8
    return input_number

# Check if the player's input matches the odd character
def is_correct_number(mistake_number, input_number):
    return mistake_number == input_number

# Convert a numeric index back to the grid notation (e.g., 8 -> D2)
def change_string(number):
    col_number = number % col               # Column = remainder when divided by total columns
    row_number = math.floor(number / col) + 1 # Row = integer division +1 for 1-based numbering
    return number_data[col_number] + str(row_number)

# Display the result of the player's choice
def view_result(is_correct, mistake_number):
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect")
        print("The correct answer is " + change_string(mistake_number))

# Main function to run the game
def play():
    section_message()  # Show current level
    mistake_number, question = view_question()  # Display grid and get odd character
    choice = input("(e.g. A1) ")  # Get player input
    print("Debug: choice = " + choice)
    input_number = change_input_number(choice)  # Convert input to linear index
    print("Debug: input_number = " + str(input_number))
    is_correct = is_correct_number(mistake_number, input_number)  # Check correctness
    view_result(is_correct, mistake_number)  # Show result

# Start the game
start_message()
play()
