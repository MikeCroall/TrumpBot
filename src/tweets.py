from twython import Twython  # pip install twython
import time, json  # standard lib
from apiKeys import CK, CS, AT, ATS

fileName = 'src/tweets.json'

CONSUMER_KEY = CK
CONSUMER_SECRET = CS
ACCESS_KEY = AT
ACCESS_SECRET = ATS
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

file = open(fileName, 'r')
jsonFile = json.loads(file.read())
file.close()

latest_id = jsonFile['lastId']
if latest_id == "UNKNOWN":
    user_timeline = twitter.get_user_timeline(screen_name="craigaddyman", count=1)
    latest_id = user_timeline[0]['id']
tweetDict = jsonFile['tweets']
tweetIDs = [latest_id]  ## this is the latest starting tweet id
for i in range(0, 16):  ## iterate through all tweets
    print("\n\n\n\nLoop " + str(i))
    ## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",
                                              count=200, include_retweets=False, max_id=tweetIDs[-1])
    if len(user_timeline) == 0:
        print("\n\nTERMINATED DUE TO NO MORE TWEETS \n\n")
        break
    time.sleep(300)  ## 5 minute rest between api calls

    for tweet in user_timeline:
        tweetDict[tweet['id']] = tweet['text']
        tweetIDs.append(tweet['id'])  ## append tweet id's

print("Total tweet count: " + str(len(tweetIDs)))
print("Last tweet ID: " + str(tweetIDs[-1]))

toWrite = json.dumps({
    "lastId": tweetIDs[-1],
    "tweets": json.dumps(tweetDict)
})

file = open(fileName, 'w')
file.truncate()
file.write(toWrite)
file.close()