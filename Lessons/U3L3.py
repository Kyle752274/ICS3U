# Modify 1 
items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
matches = []

for i in range(len(items)): 
  sizeI = len(items[i])
  sizes.append(sizeI)

for i in range(len(sizes)):
  if sizes[i] == len(items[i]):
    matches.append(True)
  else:
    matches.append(False)

for i in range(len(sizes)):
  print("%d %s, %s" % (sizes[i], items[i], matches[i]))
