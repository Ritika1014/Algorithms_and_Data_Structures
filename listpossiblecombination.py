from itertools import permutations

# Predefined list
lst = [1, 2, 3]

# Generate all possible permutations
combinations = list(permutations(lst))

# Display results
print("All possible combinations:")
for c in combinations:
    print(c)

# Display the number of combinations
print("Total number of combinations:", len(combinations))
