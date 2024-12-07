# Imports turtle 
import turtle
# Sets turtle background color
turtle.bgcolor("gray40")
# Turns off updates to speed up plotting
turtle.tracer(0, 0)
# Sets turtle to t variable
plotter = turtle.Turtle()
# Hides the plotter sprite
plotter.hideturtle()

def modify(line):
    cleaned_line = ""
    unwanted_chars = ['"', ',']
    line = line.strip()
    for char in line:
        if char not in unwanted_chars:
            cleaned_line += char
    return cleaned_line

def plotIt(plotter, x_coord, y_coord, dot_size, dot_color):
    plotter.penup()
    plotter.goto(x_coord, y_coord)
    plotter.pendown()
    plotter.dot(dot_size, dot_color)
    plotter.penup()

def drawImage(image, pixel_size, num_rows, num_cols, x_dir, y_dir):
    x_offset = int(-num_cols // 2)
    y_offset = int(-num_rows // 2)
    for row_index in range(len(image)):
        y_offset += 1
        for col_index in range(len(image[row_index])):
            plotIt(plotter, x_offset * pixel_size * x_dir, -y_offset * pixel_size * y_dir, pixel_size, image[row_index][col_index])
            x_offset += 1
        x_offset = int(-num_cols // 2)
      
def getImageData(file_handler, num_rows, color_mappings):
    image_data = []
    for _ in range(num_rows):
        row = file_handler.readline()
        row = modify(row)
        row_colors = []
        for symbol in row:
            for mapping in color_mappings:
                if symbol == mapping[0]:
                    symbol = mapping[1]
            row_colors.append(symbol)
        image_data.append(row_colors)
    return image_data

def getColorData(file_handler, color_count):
    color_mappings = []
    for _ in range(color_count):
        line = file_handler.readline()
        line = modify(line)
        symbol, _, color = line.split()
        if symbol == '~':
            symbol = ' '
        color_mappings.append([symbol, color])
    return color_mappings

file_name = ""
is_rotated = False
is_valid = False

while not is_valid:
    user_choice = input("Choose an option to draw: \n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a file name \n")
    if user_choice.lower() == 'a':
        file_name = "rocky_bullwinkle_mod.xpm"
        is_valid = True
    elif user_choice.lower() == 'b':
        file_name = "smiley_emoji_mod.xpm"
        is_valid = True
    elif user_choice.lower() == 'c':
        file_name = input("Enter the file name: ")
        is_valid = True

file_handler = None
try:
    file_handler = open(file_name, "r")
except:
    print("File not found.")
    exit()

is_valid = False
while not is_valid:
    user_choice = input("Would you like to rotate the image (Y/N): ")
    if user_choice.lower() == 'y':
        is_rotated = True
        is_valid = True
    elif user_choice.lower() == 'n':
        is_valid = True

header_line = file_handler.readline()
header_line = modify(header_line)
num_cols, num_rows, color_count = (0, 0, 0)
if len(header_line.split()) == 4:
    num_cols, num_rows, color_count, _ = header_line.split()
else:
    num_cols, num_rows, color_count = header_line.split()

num_rows = int(num_rows)
num_cols = int(num_cols)
color_count = int(color_count)

color_mappings = getColorData(file_handler, color_count)
image_data = getImageData(file_handler, num_rows, color_mappings)
file_handler.close()

print("\nDimensions: %d x %d" % (num_rows, num_cols))
print("Number of colors:", color_count)
print("Colors:", color_mappings)

if is_rotated:
    drawImage(image_data, 3, num_rows, num_cols, -1, -1)
else:
    drawImage(image_data, 3, num_rows, num_cols, 1, 1)
turtle.update()
