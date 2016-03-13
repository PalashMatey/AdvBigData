from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy
from tweepy.api import API
import time

#consumer key, consumer secret, access token, access secret.
API_KEY="ZonlGH1oPGQ970D7r2N51yr9B"
API_SECRET="mSp4bLwRPu0ZyoxzaLNpKR2KHbn1vHh6PY5NoGs0BkghqUF2oj"
ACCESS_TOKEN="594524977-indnnrhEIakq4WlFGX49bdfH2gnhGud2mQ7oA9NQ"
ACCESS_TOKEN_SECRET="tAfbdQjSibNOIwbIbTZBDwCOsMqnoOimYqOQQVPCGzs2E"


key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
start = time.time()
start = time.time()
class Stream2Screen(tweepy.StreamListener):

    def on_status(self, status):
       	print status.text.encode('utf8')
	if (time.time()-start) > 1800:
		exit()


stream = tweepy.streaming.Stream(key, Stream2Screen())
stream.filter(track=['google'])
		
