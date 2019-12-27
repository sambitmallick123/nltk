import tweepy
from textblob import TextBlob

#consumer key, consumer secret, access token, access secret.
# Step 1 - Authenticate
consumer_key= "<##Check with Sambit for key and secret##>"
consumer_secret= <##Check with Sambit for key and secret##>

access_token="90417751-3Jy9wwyiSc85lZkYRG0LNowQUTztrJ26HiNvidEW9"
access_token_secret="oQ7v9UcLmpmW1HDLLNaxCtc5xpqw23CY3FhcvsqFCRnOy"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('india')


for tweet in public_tweets:
    print(tweet.text.encode('unicode-escape').decode('UTF-8'))
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")


