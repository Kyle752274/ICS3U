# Modify 1
N = int(input("Please Input a value: "))
factorial = N
count = N
while (count > 0):
  count -= 1
  if (count != 0):
    factorial *= count
print("%d = %d" % (N, factorial))
# Modify 2
N2 = int(input("Input a value: "))
N_count = 1
while (N_count <= N2):
  factorial = N_count
  count = N_count
  while (count > 0):
    count -= 1
    if (count != 0):
      factorial *= count
  print("%d = %d" % (N_count, factorial))
  N_count += 1

# Modify 3
N3 = int(input("Input a value: "))
N3_count = 0
while (N3_count <= N3):
  factorial3 = N3_count
  count3 = N3_count
  while (count3 > 0):
    count3 -= 1
    if (count3 != 0):
      factorial3 *= count3
      if (count3 == 0):
        factorial3 = 1
  print("%d = %d" % (N3_count, factorial3))
  N3_count += 1
