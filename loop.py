# Loop
magicians = ['alice', 'david', 'carolina']

# "For every magician in the list of magicians, print the magician's name"
for magician in magicians:
    print(magician)

# Inner an outer indentation
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
