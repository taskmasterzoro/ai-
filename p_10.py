# Import necessary modules
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatizing words
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))

# 'a' denotes adjective in 'pos'
print("better :", lemmatizer.lemmatize("better", pos="a"))
