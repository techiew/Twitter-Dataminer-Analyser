## Twitter Dataminer & Analyser
A set of python scripts that use the [Tweepy API](https://www.tweepy.org/) to mine data from the specified Twitter accounts, and then analyses that data using APIs such as [Google Cloud APIs](https://cloud.google.com/apis) and [AYLIEN Sentiment Analysis API](https://aylien.com/news-api/). Specifically, it grabs 200 of that account's latest tweets and stores the data for each one, such as the text, hashtags, number of times the tweet has been retweeted, and so on.

After the data has been mined, it will store that data into a .json file for further processing. This .json file will be used as input for the analysation scripts. The analysation scripts
