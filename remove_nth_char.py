# Remove nth index character from a string

# Input string and index
string = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

# Check if index is valid
if 0 <= n < len(string):
    new_string = string[:n] + string[n+1:]
    print("String after removing character:", new_string)
else:
    print("Invalid index!")
