import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from elasticsearch import Elasticsearch
from kafka import KafkaProducer
from kafka.errors import KafkaError


class listener(StreamListener):

	es = Elasticsearch()

	tweet_producer = KafkaProducer()

	def on_data(self, raw_data):

		json_data = json.loads(raw_data)
		if json_data.get("text", None) is not None:

			co = json_data["coordinates"]
			lang = json_data["lang"]
			text = json_data['text']

			if (co is not None) and lang == "en":

				tweet_data = {}

				tweet_data["location"] = co["coordinates"]

				tweet_data["text"] = text

				json_tweet_data = json.dumps(tweet_data)

				future = self.tweet_producer.send("Tweets", bytes(json_tweet_data, 'utf-8'))

				try:
					future.get(timeout=10)
				except KafkaError:
					print("Exception occurred")
					pass

		return True

	def on_error(self, status_code):
		print(status_code)

	def on_disconnect(self, notice):
		print(self.s)


def main():
	c_key = "dw9w6y9O432ndFsBe3Dfu5LR1"
	c_secret = "bremcvPZ7I5WOh9vyHyLOo8R2BNRXKVZ3bfldareVx97kKT1wL"
	a_token = "147592347-gpKOcO2bDcwPI55bUBgjQ2u57qlZjWiowhu9D3H3"
	a_secret = "YJIpb3tuTmMkVq5Qcbhb625whnQJeZagoZrFx82p0jgBi"
	auth = OAuthHandler(c_key, c_secret)
	auth.set_access_token(a_token, a_secret)

	tweets = tweepy.Stream(auth, listener())
	tweets.filter(
		track=["trump", "instagram", "NBA", "food","google", "NYC", "travel", "football", "cricket"],
		async=True)


if __name__ == "__main__":
	main()
