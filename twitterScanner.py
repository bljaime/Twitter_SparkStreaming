import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import socket
import json

# Fill out your consumer & consumer secret API keys,
# access & access secret token keys.

consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '

# It's going to listen

class TweetListener(StreamListener):
    
    def __init__(self, csocket):
        self.client_socket = csocket
    
    def on_data(self,data):
        
        try:  # Once we get a connection:
            msg = json.loads(data)  # Use the json library to load that data
            print(msg['text'].encode('utf-8'))  # Send msg through the socket
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("ERROR ", e)
    
    def on_error(self, status):
        print(status)
        return True

# Connecting to Twitter and filter everything by a certain string

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)
  
  # Launching Tweeter Stream
  twitter_stream = Stream(auth, TweetListener(c_socket))
  # Filtering out those tweets which countain the word guitar
  twitter_stream.filter(track=['art'])

if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'  # locally..!
    port = 9998
    s.bind((host, port))
    print('listening on port 9998')
    s.listen(5)
    c, addr = s.accept()
    sendData(c)  # Send the data to the client socket
