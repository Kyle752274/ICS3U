n = int(input("Please Input An Integer:"))
print("Counting from j = 1 to %d: " % n)
print("%1s %5s %10s" % ("j", "tri", "factorial"))
for J in range(1, n + 1):
  tri = 0
  fac = 1
  for i in range(1, J + 1):
    tri += i
    fac *= i
  print("%1s %5s %10s" % (str(J), str(tri), str(fac))) 
