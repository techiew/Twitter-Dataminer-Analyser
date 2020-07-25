import json
import os.path
import sys
import time
from aylienapiclient import textapi
from aylienapiclient.errors import HttpError

# AYLIEN credentials
application_id = "XXXXXXXXXXX"
application_key = "XXXXXXXXXXXX"

def performSentimentAnalysis(jsonFile):
    client = textapi.Client(application_id, application_key)
    analysedTweets = {}
    analysedTweets["metadata"] = {}
    analysedTweets["analysedTweets"] = {}
    positiveTweets = 0
    negativeTweets = 0
    neutralTweets = 0

    with open(jsonFile, encoding = "utf-8") as file:
        data = json.load(file)

    iteration = 0
    retries = 0

    for tweet_id, tweet_data in data.items():

        print(iteration)
        time.sleep(2)

        text = tweet_data.get("translatedText").encode("utf-8", errors = "ignore")
        text = text[2:len(text)-1]

        try:
            response = client.Sentiment({"text": text})
        except HttpError:
            print(HttpError)
            print("HTTP error, continuing...")
            if(retries >= 20):
                break
            retries += 1
            time.sleep(20)
            continue

        remaining = client.RateLimits().get("remaining")
        print(client.RateLimits())

        if(remaining != None):
            if(remaining <= 0):
                print("Ended at: ")
                print(iteration)
                break

        if(response.get("polarity") == "positive"):
            positiveTweets += 1
        elif(response.get("polarity") == "negative"):
            negativeTweets += 1
        else:
            neutralTweets += 1

        analysedTweets["analysedTweets"][tweet_id] = response
        iteration += 1

    analysedTweets["metadata"]["positiveTweets"] = positiveTweets
    analysedTweets["metadata"]["negativeTweets"] = negativeTweets
    analysedTweets["metadata"]["neutralTweets"] = neutralTweets

    with open((jsonFile + "_sentiment_analysis").replace(".json", "") + ".json", "w", encoding = "utf-8") as file:
        json.dump(analysedTweets, file, sort_keys = False, indent = 4, default = str)

    print("Sentiment analysis complete!")

if __name__ == '__main__':

    if(len(sys.argv) < 2):
        print("Args: source json file (include .json)")
        sys.exit()

    if(os.path.exists(sys.argv[1]) & os.path.isfile(sys.argv[1])):
        performSentimentAnalysis(sys.argv[1])
