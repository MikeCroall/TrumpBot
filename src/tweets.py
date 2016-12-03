from twython import Twython  # pip install twython
import time  # standard lib
from apiKeys import CK, CS, AT, ATS

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = CK
CONSUMER_SECRET = CS
ACCESS_KEY = AT
ACCESS_SECRET = ATS
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

user_timeline = twitter.get_user_timeline(screen_name="craigaddyman", count=1)
latest_id = user_timeline[0]['id']

tweetIDs = [latest_id]  ## this is the latest starting tweet id
for i in range(0, 16):  ## iterate through all tweets
    print("Loop " + str(i))
    ## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",
                                              count=200, include_retweets=False, max_id=tweetIDs[-1])
    time.sleep(300)  ## 5 minute rest between api calls

    for tweet in user_timeline:
        print(tweet['text'])  ## print the tweet
        tweetIDs.append(tweet['id'])  ## append tweet id's

print("Total tweet count: " + str(len(tweetIDs)))
print("Last tweet ID: " + str(tweetIDs[-1]))
