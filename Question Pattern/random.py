import random

# Generate a random number either 0 or 1
random_number = random.randint(0, 1)

# Map 0 to -1 and 1 to 1
result = 2 * random_number - 1

print(result)
