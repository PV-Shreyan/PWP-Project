import os
import time
import random
import logging
import tweepy

from dotenv import load_dotenv
load_dotenv()

#  1. Load API Keys & Tokens.
API_KEY = os.getenv ("API_KEY")
API_KEY_SECRET = os.getenv ("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv ("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv ("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv ("BEARER_TOKEN")

#  2. Authenticate the Tweepy Client.
client = tweepy.Client (
    bearer_token = BEARER_TOKEN,
    consumer_key = API_KEY,
    consumer_secret = API_KEY_SECRET,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
)

#  3. Setup of Logger.
logging.basicConfig (
    filename = "bot.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger ()

#  4. Predefined Tweets and Tweet's IDs'.
TWEET_PHRASES = [
    # Add the Tweets here.
    "Embrace the chaos!!",
    "Another random thought from my amazing mind!",
    "Coding is like magic, except ur spells have more syntax errors.",
    "Stay humble. Stay cool",
    "Hello World!!!."
]

RETWEET_TARGETS = [
    # Add Tweet's IDs' here.
    1986215386224992320,
    1986400282461548863,
    1986593526059311604
]

#  5. Creating User-defined Functions.
def random_delay (min_seconds = 30, max_seconds = 120):
    # Pause for a random number of seconds between 30-120 secs.
    
    delay = random.uniform (min_seconds, max_seconds)
    logger.info (f"Sleeping for {delay:.2f}.")
    time.sleep (delay)


def tweet_random_phrase():
    # Post a random tweet from the predefined list.
    
    phrase = random.choice (TWEET_PHRASES)
    try:
        client.create_tweet (text = phrase)
        logger.info (f"Tweeted successfully: {phrase}")
        print (f"Tweeted: {phrase}")
        
    except Exception as e:
        logger.error (f"Error tweeting: {e}")
        print (f"Error tweeting: {e}")


def retweet_random_post():
    # Retweet a random tweet ID from the target list.
    
    if not RETWEET_TARGETS:
        logger.warning ("No retweet targets found.\n")
        print ("No retweet targets configured.")
        return

    tweet_id = random.choice (RETWEET_TARGETS)
    try:
        client.retweet (tweet_id = tweet_id)
        logger.info (f"Retweeted successfully: {tweet_id}.\n")
        print (f"Retweeted: {tweet_id}.")
        
    except Exception as e:
        logger.error (f"Error retweeting: {e}\n")
        print (f"Error retweeting: {e}")

#  6. Main Bot Execution.
if (__name__ == "__main__"):
    print ("Twitter bot has started! Press Ctrl + C to stop.")
    logger.info ("\nTwitter bot has started.")

    try:
        while True:
            # 1) Decide randomly whether to tweet or retweet.
            chance = random.random()

            if chance < 0.5:
                logger.info("Selected to post a tweet.")
                tweet_random_phrase()
            else:
                logger.info("Selected to retweet a post.")
                retweet_random_post()

            # 2) Wait a random amount of time.
            if chance < 0.3:
                random_delay() # wait for the given default time.
            elif chance < 0.6:
                random_delay(60, 180) # wait between 1–3 mins before retweeting.
            else:
                random_delay(300, 600) # wait between 5-10 mins before retweeting. 

    except KeyboardInterrupt:
        # Exit when user enters Ctrl + C
        print("\nTwitter bot stopped manually by the user.")
        logger.info("Bot stopped manually by the user.")
        print("All actions have been logged in bot.log.")
