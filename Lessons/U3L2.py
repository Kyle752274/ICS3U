# Sample Code
items = ["Apples", "Bananas", "Cherries", "Dosa"]
print(items) # Predict A - Does this really print anything?
print("The number of items is %d." % len(items)) # Predict B
for i in items: # Predict C
    print(i)

for c in range(len(items)): # Prediction D
    print(c, items[c])

# Modify 1
items = []
item_amount = int(input("How many items are you entering? "))
print("Enter your items now: ")
for item in range(item_amount):
  items.append(input("Next item: "))
print("You have entered %d items." % len(items))
for item in items:
  print(item)
