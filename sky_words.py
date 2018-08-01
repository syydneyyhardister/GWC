'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
tweets = []#empty list/array

# Continue your program below!
for tweet in tweetData:
	tweets.append(tweet["text"])#string of twitter text
giant_string = " ".join(tweets)

# Dictionary of the frequency of each word
# key = words, value = count/ frequency of the words appearance
list_of_words = giant_string.split()

positive = []
negative = []
neutral = []

# hold the counts for each state
for word in list_of_words:
    word = word.lower().rstrip().lstrip()
    if "http" in word:
        continue
    if word[0] in {",", "?", ".", ":", "/", "!", '"', "'", "#", "@"}:
        word = word[1:]
    if len(word) < 4:
        continue
    if word[-1] in {",", "?", ".", ":", "/", "!", '"', "'"}:
        word = word[:-1]

    word_polarity = TextBlob(word).polarity
    if word_polarity < -0.25:
        negative.append(word)
    elif word_polarity < 0.25:
        neutral.append(word)
    else:
        positive.append(word)


word_count = {}
for word in list_of_words:
    word_count[word] =  word_count.get(word, 0) + 1

word_count_2 = {}
for word, count in word_count.items():
    if count < 2:
        continue
    else:
        word_count_2[word] = count
print(word_count_2)

wordcloud = WordCloud().generate_from_frequencies(word_count_2)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()

negative = {}
for word, count in negative.items():
    if count < 2:
        continue
    else:
        negative[word] = count
print(negative)

wordcloud = WordCloud().generate_from_frequencies(negative)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()

neutral = {}
for word, count in neutral.items():
    if count < 2:
        continue
    else:
        neutral[word] = count
print(neutral)

wordcloud = WordCloud().generate_from_frequencies(neutral)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()

positive = {}
for word, count in positive.items():
    if count < 2:
        continue
    else:
        positive[word] = count
print(positive)

wordcloud = WordCloud().generate_from_frequencies(positive)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()











tb = TextBlob(giant_string)
