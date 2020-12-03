## Twitter Dataminer & Analyser

This project consists of a set of python scripts. The first script uses the [Tweepy API](https://www.tweepy.org/) to mine/fetch data from a specified Twitter account, the script grabs 200 of the specified account's latest tweets and stores the data for each one, such as the text, hashtags, number of times the tweet has been retweeted, and so on. 

[![Thumbnail](https://github.com/techiew/Twitter-Dataminer-and-Analyser/blob/master/thumbnail.png)](https://www.youtube.com/watch?v=G-7zbVIuYl0)

Here's an example of a tweet that has been fetched using Tweepy:

'''json
"1060934916651790336": {
        "hashtags": [],
        "created_at": "2018-11-09 16:39:30",
        "retweet_count": 9,
        "text": "Klokt skrevet @FRI_HET https://t.co/dSVhfCJmpo",
        "user_mentions": [
            {
                "id_str": "1683115626",
                "name": "FRI",
                "id": 1683115626,
                "screen_name": "FRI_HET",
                "indices": [
                    14,
                    22
                ]
            }
        ],
        "retweeted": false,
        "favorite_count": 34,
        "url": "https://twitter.com/erna_solberg/status/1060934916651790336"
    },
'''

After the data has been mined by the first script, it will store that data into a .json file for further processing. This .json file will be used as input for the translation and analysation scripts. The scripts then translate and analyse that data by using [Google Cloud APIs](https://cloud.google.com/apis) and the [AYLIEN Sentiment Analysis API](https://aylien.com/news-api/). The resulting data would then be put on the website in the video below in the form of various graphs so that we could show our results to the teacher.
