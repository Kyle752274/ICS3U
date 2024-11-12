def factorize(N):
  factors = []
  for j in range(1, N):
    if N % j == 0:
      factors.append(j)
  return factors

# test values to test your program
print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))

# Input parameter
def factorize(N):
  factors = []
  for j in range(1, N):
    if N % j == 0:
      factors.append(j)
  return factors
  
try:
  n = int(input("Please enter a positive integer: "))
  print(factorize(n))
except:
  print("Please input a valid number")
  
  # Make more
def factorize(N):
  factors = []
  for j in range(1, N):
    if N % j == 0:
      factors.append(j)
  return factors
  
def sum(N):
  amount = 0
  for i in N:
    amount += i
  return amount

try:
  n = int(input("Please enter a positive integer: "))
  if n > 0:
    n_factors = factorize(n)
    n_sum = sum(n_factors)
    print("Factor sum: %d" % n_sum)
    if n_sum == n:
      print("%d is perfect" % n)
    elif n_sum > n:
      print("%d is abundant" % n)
    elif n_sum < n:
      print("%d is deficient" % n)
  else:
    print("Please input a valid number") 
except:
  print("Please input a valid number") 
