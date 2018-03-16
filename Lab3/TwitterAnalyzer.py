import json
import re
import operator
import nltk
import string

from collections import Counter


nltk.download("stopwords")  # download the stopword corpus on our computer

from nltk.corpus import stopwords

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
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'a', '…', 'q']
fname = 'ArtificialIntelligenceTweets.json'
with open(fname, 'r') as f:
    count_all_tokens = Counter()  # counter for all tokens
    count_terms_hash = Counter()  # counter for hashtags
    count_terms = Counter()  # counter for terms excluding hashtags and mentions
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        all_tokens = [term for term in preprocess(tweet['text'], True) if term not in stop]
        terms_hash = [term for term in preprocess(tweet['text'], True) if term not in stop and term.startswith('#')]
        terms = [term for term in preprocess(tweet['text'], True) if term not in stop and not term.startswith(('#', '@'))]
        count_all_tokens.update(all_tokens)
        count_terms_hash.update(terms_hash)
        count_terms.update(terms)
    print ('List of the top ten most frequent tokens\n')
    for word, index in count_all_tokens.most_common(10):
        print('%s : %s' % (word, index))
    print ('\nList of the top ten most frequent hashtags\n')
    for word, index in count_terms_hash.most_common(10):
        print('%s : %s' % (word, index))
    print ('\nList of the top ten most frequent terms, skipping mentions and hashtags\n')
    for word, index in count_terms.most_common(10):
        print('%s : %s' % (word, index))
