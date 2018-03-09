# Lab2 - ReadMe

#### GroupId
1102

#### Members & email
- Syeda Noor Zehra Naqvi         <syeda.noor.zehra.naqvi@est.fib.upc.edu>
- Todi Thanasi                   <todi.thanasi@gmail.com>
                         
#### Github url
https://github.com/todithanasi/CLOUD-COMPUTING-CLASS-2018

#### Additinonal comments


#### Task 2.1.1: Word Count 1 - Output
```
The most 10 frequent words are:  [('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 468), (':', 454), ('in', 417)]
Total number of words is: 25155
```

#### Task 2.1.2: Remove punctuation - Output
```
The most 10 frequent words are: [('the', 1444), ('of', 586), ('to', 531), ('in', 506), ('a', 481), ('and', 346), ('is', 289), ('we', 279), ('that', 275), ('this', 268)]
Total number of words is: 19593
```

#### Task 2.1.3: Stop Words - Output
Tensorflow is not the most frequent word because in the calculation of the words count are included all the possible tokens in the text, said that even the 
English prepositions, articles, adverbs etc which probably take a bigger percentage in the text than the actual frequent words.

```
The english stopwords in the text are: ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
The most 10 frequent words are: [('tensorflow', 193), ('data', 102), ('tensor', 99), ('code', 90), ('learning', 81), ('function', 74), ('one', 73), ('use', 65), ('example', 64), ('available', 63)]
Total number of words is: 11220
```

#### Task 2.2.1: Accessing your twitter account information - Output
Yes the received data from the tweepy API were correct. Find below the result of it.

```
Name: Noor Zehra
Location: Islamabad, Pakistan
Friends: 40
Created: 2013-10-19 07:50:38
Description: 
```

#### Task 2.2.2: Accessing Tweets - Output

The below code is accessing the tweets from the home timeline (the tweets from the entities that user is following and are appearing on the their home). 
In the below code we return only the first tweet in text format.

```
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)
```

The below code is accessing the 10 latest tweets from the home timeline. It return the information in JSON format.
```
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(json.dumps(status._json, indent=2))
```

The below code is used to get friends and their information like name, description, location, number of their friends etc  in JSON format. In the example we return only 15 of the account's friends, the one that we are following.
```
for friend in tweepy.Cursor(api.friends).items(15):
    print(json.dumps(friend._json, indent=2))
```

We have used this code to access the 10 latest tweets that user have posted in his account, in JSON format.
```
for tweet in tweepy.Cursor(api.user_timeline).items(5):
    print(json.dumps(tweet._json, indent=2))
```

#### Task 2.3: Tweet pre-processing - Output




