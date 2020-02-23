import json
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np


tweets_filename = 'remaintweets1.txt'
tweets_file = open(tweets_filename, "r")

brexitTweets = []
for line in tweets_file:
    try:
       brexitTweets.append(json.loads(line))
    except:
        continue

print(len(brexitTweets))

zero =0
tweetsDF = pd.DataFrame()
tweetsDF['text'] = list(map(lambda tweet: tweet['text'], brexitTweets))
tweetsDF['lang'] = list(map(lambda tweet: tweet['lang'], brexitTweets))
tweetsDF['full_name'] = list(map(lambda tweet: tweet['place']['full_name']if tweet['place'] != None else None , brexitTweets))
tweetsDF['favourites_count'] = list(map(lambda tweet: tweet['user']['screen_name']if tweet['user']['favourites_count'] >= zero else None, brexitTweets))
tweetsDF['retweet_count'] = list(map(lambda tweet: tweet['user']['screen_name']if tweet['retweet_count'] != None else None, brexitTweets))

tweetsDF['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, brexitTweets))
tweetsDF.describe()


tweets_by_cities = tweetsDF['retweet_count'].value_counts()
tweets_by_cities[:5].plot(kind='pie', label='')
plt.show()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Names', fontsize=25)
ax.set_ylabel('Number of retweets', fontsize=10)
ax.set_title(' Most Retweeted tweets', fontsize=15, fontweight='bold')
tweets_by_cities[:5].plot(ax=ax, kind='bar', color='blue')
tweets_by_cities = tweetsDF['screen_name'].value_counts()

