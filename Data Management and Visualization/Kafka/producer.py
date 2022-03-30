import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
from json import dumps
import time

# twitter setup (key personali eliminate)
consumer_key = "***"
consumer_secret = "***"
access_token = "***"
access_token_secret = "***"

# Authenticate with the OAuth protocol
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

topic = "Olimpiadi"

class MyListener(StreamListener):

	def __init__(self, producer, producer_topic):
		super().__init__()
		self.producer = producer
		self.producer_topic = producer_topic

	def on_status(self, status):
		if not status.truncated:
			texttweet = status.text
		else:
			texttweet = status.extended_tweet['full_text']
		tweet = {
		  'user_id': status.user.id,
		  'username': status.user.name,
		  'language':status.lang,
		  'timestamp':str(status.created_at),
		  'geo':status.geo,
		  'coordinates':status.coordinates,
		  'user_location':status.user.location,
		  'is_a_retweet': str(hasattr(status,"retweeted_status")),
		  'screen_name': status.user.screen_name,
		  'text': texttweet,
		  'hashtags': []
		}
		if status.entities.get('hashtags') is not None:
			hashtags = status.entities.get('hashtags')
			tweet['hashtags'] = [ h.get('text') for h in hashtags ]
		self.producer.send(topic=self.producer_topic, value=tweet)

	def on_error(self,status):
		print(status)

	def on_exception(self, exception):
		print(exception)
		return

def start_stream():
	while True:
		try:
			api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
			listener = MyListener(producer=producer, producer_topic=topic)
			stream = Stream(auth = api.auth, listener=listener)
			stream.filter(languages=["it"], track=['#Olimpiadi', '#ItaliaTeam', '#Tokyo2020', '#GiochiOlimpici'])
		except:
			continue

start_stream()
