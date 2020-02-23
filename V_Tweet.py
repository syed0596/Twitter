try:
    import json
except ImportError:
    import simplejson as json

# Read in the file saved from last step
tweets_filename = '0tweetsOnBrexitJan19.txt'
tweets_file = open(tweets_filename, "r")

# Tidy up the tweets so they're easier to read
for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object
        tweet = json.loads(line.strip())

        # only messages containing a 'text' field are displayed

        if 'text' in tweet:
                if 'leave' in tweet['text']:

                    brexitFile = open('leavetweets.txt', 'a')
                    brexitFile.write(line)
                    brexitFile.close()
                    print(tweet['id'])  # the tweet's id
                    print(tweet['created_at'])  # when the tweet was posted
                    print(tweet['text'])  # content of the tweet

                    print(tweet['user']['id'])  # id of the user who posted the tweet
                    print(tweet['user']['name'])  # name of the user
                    print(tweet['user']['screen_name'])  # name of the user account

                    hashtags = []
                    for hashtag in tweet['entities']['hashtags']:
                        hashtags.append(hashtag['text'])
                        print(hashtags)

                elif 'remain' in tweet['text']:
                    APFile = open('remaintweets1.txt', 'a')
                    APFile.write(line)
                    APFile.close()






    except:
        # if line read is not in JSON format, an exception may be thrown (we'll ignore here)
        continue
