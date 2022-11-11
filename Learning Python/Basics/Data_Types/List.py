# Create

fruit = ["apples","oranges","bananas"]
fruit = []
fruit = list()

# Read
fruit = ["apples","oranges","bananas"]
print(fruit[1])

# Length
len(fruit)

print(fruit[-1])
print(fruit[-2])

# Update
fruit.append("kiwi")
print(fruit)

fruit.insert(2, "passion fruit")
print(fruit)

# Organizing a list
print(sorted(fruit))
print(fruit)

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

# Delete
del fruit[1]
print(fruit)

favorite_fruit = fruit.pop()
print(favorite_fruit)

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

fruit.remove('bananas')
print(fruit)