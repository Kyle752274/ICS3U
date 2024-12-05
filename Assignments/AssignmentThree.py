import turtle

# Set up the turtle environment
turtle.bgcolor("gray40")
turtle.tracer(0, 0)
pen = turtle.Turtle()
pen.hideturtle()

# Clean up the string by removing unwanted characters
def sanitize_input(line):
    cleaned_line = ""
    forbidden_chars = ['"', ',']
    line = line.strip()
    for char in line:
        if char not in forbidden_chars:
            cleaned_line += char
    return cleaned_line

# Plot a colored dot at a specific coordinate
def draw_dot(turtle, x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(size, color)
    turtle.penup()

# Render the image using the color map and coordinates
def render_image(data, pixel_size, rows, cols, rotate_x, rotate_y):
    x_offset = -cols // 2
    y_offset = -rows // 2
    for i in range(len(data)):
        row = data[i]
        y_offset += 1
        for j in range(len(row)):
            color = row[j]
            draw_dot(pen, x_offset * pixel_size * rotate_x, -y_offset * pixel_size * rotate_y, pixel_size, color)
            x_offset += 1
        x_offset = -cols // 2

# Read the image data (pixels and colors)
def extract_image_data(file_handle, row_count, color_map):
    pixel_data = []
    for _ in range(row_count):
        row = file_handle.readline()
        sanitized_row = sanitize_input(row)
        pixel_row = []
        for char in sanitized_row:
            color = char
            for color_code in color_map:
                if color == color_code[0]:
                    color = color_code[1]
            pixel_row.append(color)
        pixel_data.append(pixel_row)
    return pixel_data

# Extract color mapping (symbols to colors)
def extract_color_mapping(file_handle, color_count):
    color_map = []
    for _ in range(color_count):
        color_info = file_handle.readline()
        sanitized_info = sanitize_input(color_info)
        parts = sanitized_info.split()
        if len(parts) >= 3:
            symbol = parts[0]
            color = parts[2]
            if symbol == '~':
                symbol = ' '
            color_map.append([symbol, color])
        else:
            print(f"Skipping invalid color definition: {sanitized_info}")
            continue  # Skip this line and proceed to the next
    return color_map

# Prompt the user to select the image and rotation option
image_file = ""
rotate_image = False

valid_input = False
while not valid_input:
    choice = input("Select an image to load: \n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a custom file name \n")
    if choice.lower() == 'a':
        image_file = "rocky_bullwinkle_mod.xpm"
        valid_input = True
    elif choice.lower() == 'b':
        image_file = "smiley_emoji_mod.xpm"
        valid_input = True
    elif choice.lower() == 'c':
        image_file = input("Please provide the image file name: ")
        valid_input = True

valid_input = False
while not valid_input:
    rotation_choice = input("Would you like to rotate the image (Y/N): ")
    if rotation_choice.lower() == 'y':
        rotate_image = True
        valid_input = True
    elif rotation_choice.lower() == 'n':
        valid_input = True

# Open the image file and parse the data
with open(image_file, "r") as file_handle:
    header = file_handle.readline()
    sanitized_header = sanitize_input(header)
    
    # Safely split header values, handling more than 3 parts
    parts = sanitized_header.split()
    if len(parts) >= 3:
        cols, rows, numColors = map(int, parts[:3])  # Use only the first three parts
    else:
        print(f"Error: Header line is malformed. Expected at least 3 parts, got {len(parts)}.")
        exit(1)

    color_map = extract_color_mapping(file_handle, numColors)
    pixel_data = extract_image_data(file_handle, rows, color_map)

# Display some basic info about the image
print(f"\nImage dimensions: {rows} rows x {cols} columns")
print(f"Number of colors: {numColors}")
print("Color definitions:", color_map)

# Draw the image based on rotation preference
if rotate_image:
    render_image(pixel_data, 3, rows, cols, -1, -1)
else:
    render_image(pixel_data, 3, rows, cols, 1, 1)

# Force the turtle to update the display
turtle.update()

# Keep the window open
turtle.done()
