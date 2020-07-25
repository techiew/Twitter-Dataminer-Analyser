import tweepy
import json
import sys
import datetime
from collections import OrderedDict

consumer_key = "XXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def getAllTweetsFromUser(twitterUsername, fileName):

    #Maks antall tweets vi kan hente ut er 3240
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    tweetList = []
    filteredData = OrderedDict()
    metadata = { "metadata": {} }

    linkUsername = twitterUsername

    if linkUsername[0] == '@':
        linkUsername = linkUsername[1:]
    else:
        twitterUsername = "@" + twitterUsername


    print("Getting tweets...")

    #Hent ut de 200 nyeste tweetsa, 200 er maks for denne metoden
    #Vi må starte med å hente ut de nyeste tweetsa slik at vi kan få oldestTweetID som vi kan bruke i loopen
    newTweets = api.user_timeline(screen_name = twitterUsername, count = 200, tweet_mode = "extended")

    #Legg disse nyeste tweetsa i lista vår
    tweetList.extend(newTweets)

    #Vi lagrer ID'en til den eldste tweeten i lista så vi vet hvor vi må starte fra senere
    oldestTweetID = tweetList[-1].id - 1

    #Loopen går igjennom alle tweetsa
    while len(newTweets) > 0:
        #Vi lager en request som før bare at max_id er nå definert
        #Med max_id definert kan vi hente ut mange flere tweets på en enkelt request
        newTweets = api.user_timeline(screen_name = twitterUsername, count = 3240, tweet_mode = "extended", max_id = oldestTweetID)
        tweetList.extend(newTweets)
        oldestTweetID = tweetList[-1].id - 1

    isRetweet = False
    tweetText = ""
    tweetCreatedAt = 0
    hashtags = ""
    userMentions = ""
    retweetCount = 0
    favoriteCount = 0
    numRetweets = 0 #Antall tweets fra denne brukeren som er retweets
    numReplies = 0
    totalSelfBeenFavorited = 0
    totalSelfBeenRetweeted = 0 #Antall ganger denne brukeren sine tweets har blitt retweeta

    for tweet in tweetList:
        tweetUrl = "https://twitter.com/" + linkUsername + "/status/" + tweet.id_str

        if "retweeted_status" in dir(tweet):
            isRetweet = True
            tweetText = tweet.retweeted_status.full_text
            tweetCreatedAt = tweet.retweeted_status.created_at
            hashtags = tweet.retweeted_status.entities.get("hashtags")
            userMentions = tweet.retweeted_status.entities.get("user_mentions")
            retweetCount = 0
            favoriteCount = 0
            numRetweets += 1
        else:
            isRetweet = False
            tweetText = tweet.full_text
            tweetCreatedAt = tweet.created_at
            hashtags = tweet.entities.get("hashtags")
            userMentions = tweet.entities.get("user_mentions")
            retweetCount = tweet.retweet_count
            favoriteCount = tweet.favorite_count
            totalSelfBeenFavorited += tweet.favorite_count
            totalSelfBeenRetweeted += tweet.retweet_count

            if tweet.in_reply_to_status_id is None:
                numReplies += 1


        filteredData.update({tweet.id_str: {"retweeted": isRetweet, "text": tweetText, "hashtags": hashtags, "user_mentions": userMentions, "created_at": tweetCreatedAt, "retweet_count": retweetCount, "favorite_count": favoriteCount, "url": tweetUrl}})

    print(str(filteredData).encode("utf8"))
    print("Number of tweets downloaded: %s" % (len(tweetList)))
    print("Writing tweets to JSON...")

    metadata["metadata"]["totalTweets"] = len(tweetList)
    metadata["metadata"]["numTweets"] = len(tweetList) - (numRetweets + numReplies)
    metadata["metadata"]["numRetweets"] = numRetweets
    metadata["metadata"]["numReplies"] = numReplies
    metadata["metadata"]["totalSelfBeenFavorited"] = totalSelfBeenFavorited
    metadata["metadata"]["totalSelfBeenRetweeted"] = totalSelfBeenRetweeted

    with open(fileName, "w", encoding = "utf-8") as file:
        json.dump(filteredData, file, sort_keys = False, indent = 4, default = str)

    with open((fileName + "_metadata").replace(".json", "") + ".json", "w", encoding = "utf-8") as file:
        json.dump(metadata, file, sort_keys = False, indent = 4, default = str)

    print("Done!")


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Args: twitter username, json file name (include .json)")
        sys.exit()

    getAllTweetsFromUser(sys.argv[1], sys.argv[2])
    #getAllTweetsFromUser("@erna_solberg", "erna.json")
