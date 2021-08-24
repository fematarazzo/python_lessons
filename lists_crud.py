# Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing first item
print(bicycles[0])

# Accessing last iteim
print(bicycles[-1])

# Using individual values from a list
message = f"My first bicycle was a {bicycles[-1].title()}."
print(message)

# CRUD
motorcycles = ['honda', 'yamaha', 'suzuki']

# Modifying element in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']

# Appending
motorcycles.append('ducati')
print(motorcycles)

# Inserting
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Removing an item using del statement
del motorcycles[0]
print(motorcycles)

# Removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Popping items from any position in a list
motorcycles = ['honda', 'yahama', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing and item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)