# Import the necessary methods from tweepy library
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from pyquery import PyQuery


# Variables that contains the user credentials to access Twitter API
consumer_key = "Pxg8ffRNFAPPMaPXcSyUAMrLl"
consumer_secret = "hubnXbrrPwP25tXaX6c2YYbNPCCqf1wThcM7whpOwra5YRUQ5Q"  # API Secret
access_token = "135161799-obzulizJnt633XpyT7BbayTuFyacA0E6tWqmO5Pw"  # Access Token
access_token_secret = "EyC0qlSdphl429T4A9asmaoRFGqYQVyjHnDlbhKfjtMIC"  # Token Secret




# This is a basic listener that just prints received tweets to stdout
class Listener(StreamListener):

# override method from tweepy.streaming
    def on_data(self, data):
        line = data
        all(s in line for s in (" brexit"))
        print(line)
        brexitFile = open('0tweetsOnBrexitJan19.txt', 'a')
        brexitFile.write(line)
        brexitFile.close()

    #def on_status(self, status):

        #print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, Listener())



stream.filter(track=['brexit'])


