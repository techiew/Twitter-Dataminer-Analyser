## Twitter Dataminer & Analyser

This project consists of a set of python scripts. The first script uses the [Tweepy API](https://www.tweepy.org/) to mine data from a specified Twitter account, the script grabs 200 of the specified account's latest tweets and stores the data for each one, such as the text, hashtags, number of times the tweet has been retweeted, and so on. 

[![Thumbnail](https://github.com/techiew/Twitter-Dataminer-and-Analyser/blob/master/thumbnail.png)](https://www.youtube.com/watch?v=G-7zbVIuYl0)

After the data has been mined by the first script, it will store that data into a .json file for further processing. This .json file will be used as input for the translation and analysation scripts. The scripts then translate and analyse that data by using [Google Cloud APIs](https://cloud.google.com/apis) and the [AYLIEN Sentiment Analysis API](https://aylien.com/news-api/). The resulting data would then be put on the website in the video below in the form of various graphs so that we could show our results to the teacher.
