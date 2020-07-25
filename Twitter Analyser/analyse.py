import json
import os.path
import sys
import string
from collections import OrderedDict

def analyseTweetsData(jsonFile):
    analysisData = {}
    analysisData["hashtagCount"] = {}
    analysisData["userMentions"] = {}
    analysisData["wordCount"] = {}
    analysisData["mostRetweetedTweetID"] = 0
    analysisData["mostFavoritedTweetID"] = 0
    data = {}
    wordFilter = [",", ".", "'"]
    stripLetters = ",.!;:-*?()[]"
    highestRetweetCount = 0;
    highestFavoriteCount = 0;

    print("Analysing...")

    with open(jsonFile, encoding = "utf-8") as file:
        data = json.load(file)

    for tweet_id, tweet_data in data.items():

        #Tell alle hashtags
        for hashtag in tweet_data.get("hashtags"):
            hashtagText = hashtag.get("text")

            if hashtagText not in analysisData["hashtagCount"]:
                analysisData["hashtagCount"][hashtagText] = 1
            else:
                analysisData["hashtagCount"][hashtagText] += 1

        #Tell alle Twitter brukere som blir nevnt i tweets
        for user in tweet_data.get("user_mentions"):
            userMentionedName = user.get("screen_name");

            if userMentionedName not in analysisData["userMentions"]:
                analysisData["userMentions"][userMentionedName] = 1
            else:
                analysisData["userMentions"][userMentionedName] += 1

        #Tell alle individuelle ord
        for word in tweet_data.get("text").split(" "):
            curWord = str(word.encode("utf-8", errors = "replace"))
            curWord.strip()

            if not len(curWord) > 0:
                continue

            curWord = curWord[2:len(curWord)-1]
            curWord = curWord.strip(stripLetters)
            curWord = curWord.translate(string.punctuation)

            if not len(curWord) > 0:
                continue

            if curWord in wordFilter:
                continue

            if ("@" in curWord) or ("#" in curWord):
                continue

            if ("https:" in curWord) or ("http:" in curWord):
                continue

            if curWord not in analysisData["wordCount"]:
                analysisData["wordCount"][curWord] = 1
            else:
                analysisData["wordCount"][curWord] += 1

        #Finn mest retweeta tweet
        retweetCount = tweet_data.get("retweet_count")
        if(retweetCount != None):
            if(retweetCount > highestRetweetCount):
                analysisData["mostRetweetedTweetID"] = tweet_id
                highestRetweetCount = retweetCount

        #Finn mest likte tweet (hjertene)
        favoriteCount = tweet_data.get("favorite_count")
        if(favoriteCount != None):
            if(favoriteCount > highestFavoriteCount):
                analysisData["mostFavoritedTweetID"] = tweet_id
                highestFavoriteCount = favoriteCount

    #Sorter arrayene i synkende rekkefølge
    analysisData["hashtagCount"] = sorted(analysisData["hashtagCount"].items(), key = lambda x: x[1], reverse = True)
    analysisData["userMentions"] = sorted(analysisData["userMentions"].items(), key = lambda x: x[1], reverse = True)
    analysisData["wordCount"] = sorted(analysisData["wordCount"].items(), key = lambda x: x[1], reverse = True)

    print(analysisData)

    with open((jsonFile + "_analysis").replace(".json", "") + ".json", "w", encoding = "utf-8") as file:
        json.dump(analysisData, file, sort_keys = False, indent = 4, default = str)

    print("Done!")

if __name__ == '__main__':

    if(len(sys.argv) < 2):
        print("Args: source json file (include .json)")
        sys.exit()

    if(os.path.exists(sys.argv[1]) & os.path.isfile(sys.argv[1])):
        analyseTweetsData(sys.argv[1])
