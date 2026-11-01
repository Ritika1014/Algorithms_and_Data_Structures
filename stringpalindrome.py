# Check if a string is palindrome or not

# Input string
string = input("Enter a string: ")

# Convert to lowercase for uniform comparison
string = string.lower()

# Check palindrome
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
