import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data files (run this once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Dummy text
txt = (
    "Sukanya, Rajib and Naba are my good friends. "
    "Sukanya is getting married next year. "
    "Marriage is a big step in one’s life. "
    "It is both exciting and frightening. "
    "But friendship is a sacred bond between people. "
    "It is a special kind of love between us. "
    "Many of you must have tried searching for a friend "
    "but never found the right one."
)

# Sentence tokenizer
tokenized = sent_tokenize(txt)

for i in tokenized:
    # Word tokenizer
    wordsList = word_tokenize(i)

    # Removing stop words
    wordsList = [w for w in wordsList if not w in stop_words]

    # POS tagging
    tagged = nltk.pos_tag(wordsList)

    print(tagged)
