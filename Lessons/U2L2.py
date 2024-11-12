x = input("Please input a whole number between 1 and 20: ")
x = int(x)
if (x >= 1 and x <= 20):
  y = input("Please input another whole number between 1 and 20: ")
  y = int(y)
  if (y >= 1 and y <= 20):
    rem = x % y
    if rem == 0:
      print("Yes!", y, "is a factor of", x)
    else:
      print("No!", y, "is not a factor of", x)
  else:
    print(y, "is outside of range. Cannot continue.")
else:
  print(x, "is outside of range. Cannot continue.") 
