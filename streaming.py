from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from settings import consumer_key, consumer_secret, access_token, access_token_secret

import json

class StdOutListener(StreamListener):
    def on_data(self, data):
        d = json.loads(data)
        print(d["text"])
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#java'])
