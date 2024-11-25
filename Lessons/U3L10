import math

def pythagorean_triple(n):
    triple = []
    if n % 2 != 0 and n >= 3:
        a = math.sqrt(n**2)
        b = math.sqrt(((n//2)*(n+1))**2)
        c = math.sqrt(((n//2)*(n+1) + 1)**2)
        triple.append(int(a))
        triple.append(int(b))
        triple.append(int(c))
        return triple
    if n % 2 == 0 and n >= 3:
        m = n**2//4
        a = n
        b = m - 1
        c = m + 1
        triple.append(int(a))
        triple.append(int(b))
        triple.append(int(c))
        return triple

max = int(input("Input a whole number: "))
for n in range(3, max + 1):
    print(pythagorean_triple(n))
