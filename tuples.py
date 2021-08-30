# Tuples - immutable lists
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuple with one element need a comma
my_t = (3,)

# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
