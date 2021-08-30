# Working with part of a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Slicing a list
print(players[0:3])

# Generating a subset
print(players[1:4])

# Omiting the first index in a slice
print(players[:4])

# Omiting the end index in a slice
print(players[2:])

# Inputing the last 3 elements
print(players[-3:])


# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Separate each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
