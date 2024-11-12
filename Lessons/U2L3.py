# Modify 1
count = 9
while (count != 0):
    count -= 1
    print(count)

# Modify 2
count = 0
while (count < 6):
  count += 1
  tri = count
  tri_count = tri - 1
  while (tri_count > 0):
    tri += tri_count
    tri_count -= 1
  suffex = "th"
  if (count == 1):
    suffex = "st"
  elif (count == 2):
    suffex = "nd"
  elif (count == 3):
    suffex = "rd"
  print("The %d%s triangular is %d" % (count, suffex, tri))
