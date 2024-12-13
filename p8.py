# Importing modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize the stemmer
ps = PorterStemmer()

# Sentence to be stemmed
sentence = "Programmers program with programming languages"

# Tokenizing the sentence
words = word_tokenize(sentence)

# Stemming each word
for w in words:
    print(w, ":", ps.stem(w))
