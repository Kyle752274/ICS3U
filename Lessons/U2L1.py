print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")
ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch == "C"):
    print("I prefer cherries")
else:
    print("Invalid input")

number = int(input("Enter a number from 1-100: "))
if (number >= 80) and (number <= 100):
  print("A")
elif (number >= 70) and (number <= 79):
  print("B")
elif (number >= 60) and (number <= 69):
  print("C")
elif (number >= 50) and (number <= 59):
  print("D")
elif (number >= 1) and (number <= 50):
  print("F")
else:
  print("Invalid number") 