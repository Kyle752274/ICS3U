import math
# Modifly 1
try:
  a = float(input("please input a number" ))
  b = float(input("please input a number: "))
  def add(a, b):
   return a + b

  print(add(a, b))

except:
  if not isinstance(float, int):
    print("Invalid Input")

# Modilfy 2
def mypow(m, n):
  return math.pow(m, n)
  
print(mypow(7, 2))
