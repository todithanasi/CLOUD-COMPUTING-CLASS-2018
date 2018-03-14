# Lab3 - ReadMe

#### GroupId
1102

#### Members & email
- Syeda Noor Zehra Naqvi         <syeda.noor.zehra.naqvi@est.fib.upc.edu>
- Todi Thanasi                   <todi.thanasi@gmail.com>
                         
#### Github url
https://github.com/todithanasi/CLOUD-COMPUTING-CLASS-2018

#### Task 3.1: Real-time tweets API of Twitter

We run the code to fetch the tweets for Artificial Intelligence. We collected 1000 tweets.

#### Task 3.2: Analyzing tweets - Counting terms

For the tasks we convert tokens to lowercase because before that we were getting 2 different entries for data one with a capital D and one with a small d
we also removed some extra single characters like ..., a and q
Following is the output:

```
List of the top ten most frequent tokens

big : 592
data : 551
#industriainterneto : 237
#blockchain : 216
analysis : 197
coffee : 196
doughnuts : 196
dunkin : 196
donuts : 196
vp : 196

List of the top ten most frequent hashtags

#industriainterneto : 237
#blockchain : 216
#ai : 189
#iot : 166
#datascience : 123
#crypto : 114
#cryptocurrencies : 112
#cryptorevolutio : 108
#microsoft : 105
#cryptocurrency : 103

List of the top ten most frequent terms, skipping mentions and hashtags

big : 592
data : 551
analysis : 197
coffee : 196
doughnuts : 196
dunkin : 196
donuts : 196
vp : 196
sherrill : 196
kaplan : 196
```

#### Task 3.3: Case study

For this task we also converted letters to lowercase only because otherwise in the graph we have 2 bars for barcelona( with capital b and small B).
Converting the letters to lowercase merged these two bars.
We would also like to point out that to save the proper image we have to first save image as a file and then show it, otherwise it saves a blank image.

```
plt.savefig('CaseStudy.png')  # Save it in a file
plt.show()                  # show it on IDE
```

The output graph of the analysis is: 

![Barcelona](https://github.com/todithanasi/CLOUD-COMPUTING-CLASS-2018/raw/master/Lab3/CaseStudy.png)


