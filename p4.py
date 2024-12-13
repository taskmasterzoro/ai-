# Take input from the user
my_str = input("Enter a string: ")

# Breakdown the string into a list of words
words = my_str.split()

# Sort the list
words.sort()

# Display the sorted words
for word in words:
    print(word)
