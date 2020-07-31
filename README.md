## Twitter Dataminer & Analyser
This project consists of a set of python scripts. The first script uses the [Tweepy API](https://www.tweepy.org/) to mine data from a specified Twitter account, specifically, the script grabs 200 of the specified account's latest tweets and stores the data for each one, such as the text, hashtags, number of times the tweet has been retweeted, and so on. 

After the data has been mined by the first script, it will store that data into a .json file for further processing. This .json file will be used as input for the analysation scripts. The analysation scripts then analyse that data by using APIs such as [Google Cloud APIs](https://cloud.google.com/apis) and [AYLIEN Sentiment Analysis API](https://aylien.com/news-api/). 

The resulting data from the analysation was to be put on a website in the form of various graphs so that it could be viewed by our teacher for the project. Below is a video of this website with Twitter data on it.

