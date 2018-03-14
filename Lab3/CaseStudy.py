import json
import re
import operator
import nltk
import string
import matplotlib as mpl
from collections import Counter
from nltk.corpus import stopwords
mpl.rcParams['figure.figsize'] = (6, 6)
import matplotlib.pyplot as plt

nltk.download("stopwords")  # download the stopword corpus on our computer

emoticons_str = r"""
    (?:
        [<>]?
        [:;=8]                          # eyes
        [\-o\*\'-]?                     # optional nose
        [\)\]\(\[dDpP/\:\>\<\}\{@\|\\]  # mouth
        |
        [\)\]\(\[dDpP/\:\>\<\}\{@\|\\]  # mouth
        [\-o\*\'-]?                     # optional nose
        [:;=8]                          # eyes
        [<>]?
        |
        <3                              # heart
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'[\w\.-]+@[\w\.-]+', # Email address
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r"\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}", # Phone number in formats
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '

    r'(?:[\w_]+)',  # other words
    r'(?:\S)',  # anything else
]


tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
fname = 'Lab3.CaseStudy.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_hash = [term for term in preprocess(tweet['text'], True) if term.startswith('#') and term not in stop]
        count_all.update(terms_hash)
# Print the first 10 most frequent words

sorted_x, sorted_y = zip(*count_all.most_common(15))
print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')

plt.savefig('CaseStudy.png')  # Save it in a file
plt.show()                  # show it on IDE