import math

print("%3s|%5s|%7s|%5s" % ("N", "SQR", "Cubes", "Roots"))
for n in range(10, 200, 15):
  sqr = n**2
  cube = n**3
  root = round(math.sqrt(n),2)
print("%3d|%5d|%7d|%5.2f" % (n, sqr, cube, root))
