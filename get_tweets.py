import tweepy
import credentials
import time
import sys


# AUTHENTICATION OF CONSUMER AND SECRET KEY
auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)

# AUTHENTICATION OF CONSUMER AND SECRET TOKEN
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)

# CONNECTING TWITTER API
api = tweepy.API(auth)

# Getting the username from sys argument
user_name = sys.argv[1]


# Get the first 3000 tweets
user = api.get_user(user_name)
id = None
count = 1
while count < 3001:
    tweets = api.user_timeline(user_name, tweet_mode="extended", max_id=id)
    for tweet in tweets:

        # We don't want the retweets
        if tweet.full_text.startswith("RT"):
            count += 1
            continue
        else:
            # Save the tweets in a file
            print(tweet.full_text + "\n")
            f = open("tweets.txt", "a", encoding="utf-8")
            f.write(tweet.full_text + "\n")
            f.close()
            count += 1
    # GETTING THE RATE LIMIT
    limit = api.rate_limit_status()
    limit = limit["resources"]["statuses"]
    limit = limit["/statuses/user_timeline"]
    remaining = limit["remaining"]
    print("Count: " + str(count))
    print("Remaining: " + str(remaining))
    time.sleep(1)

    id = tweet.id
    print(id)
