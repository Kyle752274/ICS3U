"""
   Author : Kyle Drnovscek
   Revision date : 30 October 2024
   Program : Yearbook assignment
   Description : Finds the most optimal perimeter for a number inputted.
   VARIABLE DICTIONARY :
     max_number (int)       = The maximum integer to check for factors
     userinput (str)        = The number of photographs inputted by the user
     perimeter (float)      = The calculated perimeter of the optimal rectangle arrangement
     factors (list)         = The list of factors of the input number
     num (int)              = factor of the input number
     x (int)                = The length of the rectangle
     y (int)                = The width of the rectangle
     done (bool)            = variable that controls the loop
"""

# Imports the math library to perform mathematical calculations
import math

# Finds factors of the input number
def factor(N):
    # List to store factors of N
    factors = []
    # Defines the maximum number 
    max_number = math.floor(math.sqrt(N))
    # Loops through all numbers from 1 up to the max_number
    for x in range(1, max_number + 1):
        # If x is a factor of N, it is added to the list
        if N % x == 0:
            factors.append(x)
    return factors

# Calculates the minimum perimeter of the rectangle with area N
def perimeter(N):
    # Gets the factors of N using the factor function
    factors = factor(N)
    # set x to 1 to find the largest factor of N 
    x = 1
    # Loop through each factor and find the largest factor in max_number
    for num in factors:
        if num > x:
            x = num
    # Calculate y
    y = N / x
    # Calculate the perimeter of the rectangle with sides x and y
    perimeter = 2 * (x + y)
    # Prints the minimum perimeter and dimensions
    print("Minimum perimeter is %d with dimensions of %d x %d" % (perimeter, x, y))

# Greet the user
print("Welcome to the school yearbook program!")
# sets done to False to control the loop
done = False

# Loops until you enter done
while not done:
    try:
        # Get the user input as a string
        userinput = (input("Please input a number of photographs: "))
        # Check if the input is done to end the program
        if userinput == "done":
            print("Goodbye!")
            done = True
            break
        # Convert input to integer
        userinput = int(userinput)
        # Check if the input is a valid positive number
        if userinput <= 0:
            print(userinput, "is not a valid number of photos")
            print("Please input a positive number")
        else:
            # Calculate the minimum perimeter if input is valid
            perimeter(userinput)
    # Handle any exceptions if input is not an integer
    except:
        print(userinput, "is not a valid number of photos")  
