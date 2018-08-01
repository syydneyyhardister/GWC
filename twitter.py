import tweepy
import random
import time

CONSUMER_KEY    = 'QmU9xbiI9GAsiDuMupo4yBtFv'
CONSUMER_SECRET = 'srZe6ZUSfluISKx8ZCQzZxCfnWUjB9MBRZ9gcv14ow5Dej7pIU'

ACCESS_TOKEN    = '1017155417716080640-SWIcY0OlOdF7i0KTXupLm4NYBGVV9T'
ACCESS_SECRET   = 'qpOlrMxYohGsBouxawALYNYVak96efr6VXv71V13xuPyg'

tweets = ["you are a snacc", "are you google? cuz i just found what i was looking for", "lookin' like a whole meal", "r u chocolate pudding? cuz u thick"]
# Authentication

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count += 1
    index = random.randint(0, len(tweets)-1)
    api.update_status(tweets[index] + str(count))
    time.sleep(5)
