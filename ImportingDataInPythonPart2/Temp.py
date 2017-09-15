'''
Created on Aug 9, 2017

@author: idolchevic
'''
print("---------------------------------------------------")
print("   API Authentication")
print("---------------------------------------------------")

# Import package
import json
import tweepy
import time

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

# Store OAuth authentication credentials in relevant variables
access_token = "776381907659583489-PCLeKYigl48MW9YOc0KbzxZeYOvX1vk"
access_token_secret = "wxT9SaGOWD5rZVQqIy4Vla7etJNvKZAy57CxNI375qAO4"
consumer_key = "asEXiw987AHoiwotg8g1pVMgs"
consumer_secret = "Qqs9tr1WLXvQXOO8ylVraFzjMT3Un4a8cCXhsa3JwbfFpU5Szq"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token,access_token_secret)


print("---------------------------------------------------")
print(" Streaming tweets  ")
print("---------------------------------------------------")
# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)

# How long do you want to stream tweets (in seconds)'''
runtime = 60 #this means one minute

stream.filter(track=['programming','code','santé','health','musk','elon','gates','innovation','game','actu','économie'], async=True)

time.sleep(runtime) #halts the control for runtime seconds

stream.disconnect() #disconnect the stream and stop streaming

print('end ?')