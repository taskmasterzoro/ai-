import string

# Given string
str = "Remove. punctuations @from a% given string?"

print("Original String :\n\t", str)

# Removing punctuations
for c in string.punctuation:
    str = str.replace(c, "")

print("After removing Punctuations :\n\t", str)
