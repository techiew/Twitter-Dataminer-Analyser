from google.cloud import translate
import json
import sys
import os.path

def translateTweetsText(jsonFile):
    data = {}
    translatedTweets = {}
    client = translate.Client()

    with open(jsonFile, encoding = "utf-8") as file:
        data = json.load(file)

    iterations = 0

    for tweet_id, tweet_data in data.items():
        translatedText = str(tweet_data.get("text").encode("utf-8", errors = "replace"))
        translatedText = translatedText[2:len(translatedText)-1]
        translatedText = client.translate(translatedText)
        translatedTweets[tweet_id] = translatedText
        print(iterations)
        iterations += 1

    print(translatedTweets)

    with open((jsonFile + "_english_translated").replace(".json", "") + ".json", "w", encoding = "utf-8") as file:
        json.dump(translatedTweets, file, sort_keys = False, indent = 4, default = str)

    print("Done!")

if __name__ == '__main__':

    if(len(sys.argv) < 2):
        print("Args: source json file (include .json)")
        sys.exit()

    if(os.path.exists(sys.argv[1]) & os.path.isfile(sys.argv[1])):
        translateTweetsText(sys.argv[1])
