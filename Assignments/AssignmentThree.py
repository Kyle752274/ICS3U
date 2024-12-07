"""
   Author : Kyle Drnovscek
   Student Number: 752274
   Revison date : 06 december 2024
   Program : Turtle Drawing Assignment
   Description : Insert file and have turtle draw it with an option to rotate it
   VARIABLE DICTIONARY :
    file_name (String): Name of the file containing the image data.
    is_rotated (Bool): Whether the image should be rotated (-1 for true, 1 for false).
    is_valid (Bool): Used to validate user input.
    user_choice (String): Stores user input for menu options or rotation choice.
    file_handler (File): Handles the reading of the input file.
    header_line (String): Stores the first line of the input file containing image dimensions and color count.
    num_rows (Integer): Number of rows in the image.
    num_cols (Integer): Number of columns in the image.
    color_count (Integer): Total number of distinct colors in the image.
    color_mappings (List): Maps symbols in the file to their corresponding colors
    image_data (List): Stores the color of each pixel row-wise after processing the input file.
    row (String): A single row read from the file before processing.
    row_colors (List): Stores the mapped colors for a single row.
    line (String): Represents a single line from the file being processed in `modify`, `getImageData`, or `getColorData`.
    cleaned_line (String): The cleaned version of a line after removing unwanted characters.
    unwanted_chars (List of Strings): List of characters to strip from a line
    symbol (String): Represents a single character or symbol from the input file.
    c (String): Placeholder for ignored data in color mappings (not used in the program).
    color (String): The color corresponding to a symbol in the color mappings.
    x_coord (Integer): X-coordinate for the turtle to plot a dot.
    y_coord (Integer): Y-coordinate for the turtle to plot a dot.
    dot_size (Integer): Size of the dot to be drawn.
    dot_color (String): Color of the dot to be drawn.
    x_offset (Integer): Starting X position for centering the image on the canvas.
    y_offset (Integer): Starting Y position for centering the image on the canvas.
    x_dir (Integer): Direction multiplier for the X-axis (1 for normal, -1 for rotation).
    y_dir (Integer): Direction multiplier for the Y-axis (1 for normal, -1 for rotation).
    pixel_size (Integer): Size of each pixel in the image (used to scale the drawing).
    row_index (Integer): Index of the current row being processed in the image data.
    col_index (Integer): Index of the current column being processed in the image data.
    i (Integer): General-purpose index variable used in loops for file handling and row processing.
"""

# Importing the Turtle graphics module
import turtle

# Set the background color of the canvas
turtle.bgcolor("gray40")

# Turn off screen updates to improve performance while plotting
turtle.tracer(0, 0)

# Create a turtle object to handle the drawing
plotter = turtle.Turtle()

# Hide the turtle cursor to make the drawing cleaner
plotter.hideturtle()

# Function to clean a line of unwanted characters such as '"' and ','
def modify(line):
    cleaned_line = ""  # Initialize the cleaned string
    unwanted_chars = ['"', ',']  # List of characters to remove
    line = line.strip()  # Remove leading/trailing whitespace
    for char in line:
        if char not in unwanted_chars:  # Check if character is not in the unwanted list
            cleaned_line += char  # Append the valid character
    return cleaned_line

# Function to plot a point (dot) on the canvas
def plotIt(plotter, x_coord, y_coord, dot_size, dot_color):
    plotter.penup()  # Lift the pen to avoid drawing lines
    plotter.goto(x_coord, y_coord)  # Move to the specified coordinates
    plotter.pendown()  # Put the pen down to draw
    plotter.dot(dot_size, dot_color)  # Draw a dot with the specified size and color
    plotter.penup()  # Lift the pen again after drawing

# Function to draw the entire image on the canvas
def drawImage(image, pixel_size, num_rows, num_cols, x_dir, y_dir):
    x_offset = int(-num_cols // 2)  # Calculate the starting X offset for centering
    y_offset = int(-num_rows // 2)  # Calculate the starting Y offset for centering
    for row_index in range(len(image)):  # Loop through each row in the image
        y_offset += 1  # Move to the next row
        for col_index in range(len(image[row_index])):  # Loop through each column
            # Plot each pixel with the corresponding color
            plotIt(plotter, x_offset * pixel_size * x_dir, -y_offset * pixel_size * y_dir, pixel_size, image[row_index][col_index])
            x_offset += 1  # Move to the next column
        x_offset = int(-num_cols // 2)  # Reset the X offset for the next row

# Function to extract image data (rows and their colors) from the file
def getImageData(file_handler, num_rows, color_mappings):
    image_data = []  # List to store image data
    for i in range(num_rows):  # Loop through the number of rows
        row = file_handler.readline()  # Read a row from the file
        row = modify(row)  # Clean the row of unwanted characters
        row_colors = []  # List to store colors for the current row
        for symbol in row:  # Loop through each character in the row
            for mapping in color_mappings:  # Map the symbol to its corresponding color
                if symbol == mapping[0]:
                    symbol = mapping[1]
            row_colors.append(symbol)  # Add the color to the row
        image_data.append(row_colors)  # Add the row to the image data
    return image_data

# Function to extract color definitions (symbol and corresponding color) from the file
def getColorData(file_handler, color_count):
    color_mappings = []  # List to store color mappings
    for i in range(color_count):  # Loop through the number of colors
        line = file_handler.readline()  # Read a line from the file
        line = modify(line)  # Clean the line of unwanted characters
        symbol, c, color = line.split()  # Split the line into symbol, c, and color
        if symbol == '~':  # If the symbol is '~', treat it as a space
            symbol = ' '
        color_mappings.append([symbol, color])  # Add the mapping to the list
    return color_mappings

# Initialize variables for the file name and rotation flag
file_name = ""
is_rotated = False
is_valid = False

# Loop to get a valid input for the file to draw
while not is_valid:
    user_choice = input("Choose an option to draw: \n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a file name \n")
    if user_choice.lower() == 'a':
        file_name = "rocky_bullwinkle_mod.xpm"  # Set file name to option A
        is_valid = True
    elif user_choice.lower() == 'b':
        file_name = "smiley_emoji_mod.xpm"  # Set file name to option B
        is_valid = True
    elif user_choice.lower() == 'c':
        file_name = input("Enter the file name: ")  # Allow the user to input a custom file name
        is_valid = True

# Try to open the selected file
file_handler = None
try:
    file_handler = open(file_name, "r")
except:
    print("File not found.")  # Exit if the file doesn't exist
    exit()

# Loop to get a valid input for whether to rotate the image
is_valid = False
while not is_valid:
    user_choice = input("Would you like to rotate the image (Y/N): ")
    if user_choice.lower() == 'y':
        is_rotated = True  # Set rotation flag
        is_valid = True
    elif user_choice.lower() == 'n':
        is_valid = True

# Read the header line to extract image dimensions and color count
header_line = file_handler.readline()
header_line = modify(header_line)
num_cols, num_rows, color_count = (0, 0, 0)
if len(header_line.split()) == 4:  # Handle cases with additional data in the header
    num_cols, num_rows, color_count, temp = header_line.split()
else:
    num_cols, num_rows, color_count = header_line.split()

# Convert extracted dimensions and color count to integers
num_rows = int(num_rows)
num_cols = int(num_cols)
color_count = int(color_count)

# Get color mappings and image data from the file
color_mappings = getColorData(file_handler, color_count)
image_data = getImageData(file_handler, num_rows, color_mappings)
file_handler.close()  # Close the file after reading

# Print image details to the console
print("\nDimensions: %d x %d" % (num_rows, num_cols))
print("Number of colors:", color_count)
print("Colors:", color_mappings)

# Draw the image on the canvas, rotating if the flag is set
if is_rotated:
    drawImage(image_data, 3, num_rows, num_cols, -1, -1)
else:
    drawImage(image_data, 3, num_rows, num_cols, 1, 1)

# Update the canvas to display the image
turtle.update()
