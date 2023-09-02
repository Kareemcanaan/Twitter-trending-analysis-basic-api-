import tweepy
from pushbullet import Pushbullet
import time
#For this you need your own api keys, Twitter gives you one freely so you dont need to pay (unless you wanna have more than one project)
# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Pushbullet API key
pushbullet_api_key = ""

# Initialize Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Initialize Pushbullet
pb = Pushbullet()

# Topic to monitor
topic_to_monitor = "YOUR_TRENDING_TOPIC"

# Function to check if the topic is trending
def is_trending(topic):
    try:
        # Query Twitter for the current tweet count of the topic
        current_tweet_count = twitter_api.search(q=topic, count=100).total_results

        # Calculate the average tweet count for the past month (simplified, as historical data is not included)
        average_tweet_count_past_month = 1000  # Replace with your actual historical data

        # Define the trending criteria (2.5x more tweets)
        trending_criteria = 2.5 * average_tweet_count_past_month

        # Check if the topic is trending
        if current_tweet_count > trending_criteria:
            return True
        else:
            return False
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        return False

# Check for trending topics at regular intervals
while True:
    if is_trending(topic_to_monitor):
        push = pb.push_note(f"Trending Topic Alert: {topic_to_monitor}", "This topic is now trending on Twitter!")
        print("Notification sent!")
    time.sleep(300)  # Sleep for 5 minutes (300 seconds)