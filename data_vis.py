'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity_values = []

for tweet in tweetData:
	tweet_text = tweet["text"]
	tb = TextBlob(tweet_text)
	print("{}: {}".format(tweet_text, tb.polarity))
	polarity_values.append(tb.polarity)

bins = [-1, -0.5, 0, 0.5, 1] #4 bins


plt.hist(polarity_values) #create a histogram #putting bins in the () makes it so that it stays in bins's parameters
plt.title("Tweet Polarity")#title
plt.ylabel("Frequency of Tweets")#label y
plt.xlabel("Polarity")
plt.grid()
plt.show()#show histogram

# Textblob sample:
#while True:
#	phrase = input("Enter a phrase: ")
#	tb = TextBlob(phrase)
#	print(tb.polarity)
