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
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

#access_token = "776381907659583489-PCLeKYigl48MW9YOc0KbzxZeYOvX1vk"
#access_token_secret = "wxT9SaGOWD5rZVQqIy4Vla7etJNvKZAy57CxNI375qAO4"
#consumer_key = "asEXiw987AHoiwotg8g1pVMgs"
#consumer_secret = "Qqs9tr1WLXvQXOO8ylVraFzjMT3Un4a8cCXhsa3JwbfFpU5Szq"

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


# Filter Twitter Streams to capture data by the keywords:
#stream.filter(track=['ia','IA', 'schovanec', 'musk', 'alexandre','TED','energie','Slidespeak'])




print("---------------------------------------------------")
print("  Load and explore your Twitter data ")
print("---------------------------------------------------")

# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())


print("---------------------------------------------------")
print("  Twitter data to DataFrame ")
print("---------------------------------------------------")

# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())



print("---------------------------------------------------")
print("  A little bit of Twitter text analysis ")
print("---------------------------------------------------")

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump',  row['text'])
    sanders += word_in_text('sanders',  row['text'])
    cruz += word_in_text('cruz',  row['text'])



print("---------------------------------------------------")
print("  Plotting your twitter datas ")
print("---------------------------------------------------")

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()


