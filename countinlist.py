# Count positive and negative numbers in a list

# Input: list of numbers
numbers = [10, -5, 8, -3, -1, 4, 0]

# Initialize counters
pos_count = 0
neg_count = 0

# Count positives and negatives
for num in numbers:
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1

# Display results
print("Positive numbers:", pos_count)
print("Negative numbers:", neg_count)
