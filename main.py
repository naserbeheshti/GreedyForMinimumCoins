# We need numpy library for better array management
import numpy as np

# initials 
# Creating coins array
coins = np.array([5, 500, 10, 20, 100,1, 200, 250, 2])
# Casting coins array to integer
coins = coins.astype(int)
# Creating target array
target = np.array([])
# Casting target array to integer
target = target.astype(int)
# Get target value from user and cast it to integer
total = int(input("Input integer value : "))
# Sort coins 
coins = np.sort(coins)[::-1]

# Running main code
for c in coins:
    if np.sum(target) > total:
        break
    while np.sum(target) < total and c<= total and np.sum(target) + c <= total :
        target = np.append(target, c)

# Show results
print(target, " -- Total value is : ", np.sum(target))
