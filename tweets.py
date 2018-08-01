import json

file = open("twitter.json", "r")
data = json.load(file)

for d in data:


    #for info_category, info in d.items():
    #for user_mention in d["user_mentions"]:
        #each user_mention is a dictionary
        #it corresponds
        #print(user_mention["text"]) #d is dictionary about tweet
        #print(d["user"]["favourites_count"])
        #print(d["text"]),
        #print(d["retweet_count"])
        
    break
