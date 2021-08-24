# Using the range() function
for value in range(1, 5):
    print(value)

# Using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# Range() third argument
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Range() and For loops
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Simple statistics with a list of numbers
digits = [1, 2, 3, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)
