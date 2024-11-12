#Modify 1 
S = "#"
for i in range (10, 0, -1):
  y = S * i
  print(y)

# Modify 2
S2 = "#"
biggest = 13
for i in range(1, biggest, 2):
    spaces = " " * int((biggest-i)/2)
    y = S2 * i
    print(spaces, y, sep = "")
# Modify 3
S3 = "#"
for i in range(biggest, 0, -2):
    spaces = " " * int((biggest-i)/2)
    y = S3 * i
    print(spaces, y, sep = "")
