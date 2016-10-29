import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from elasticsearch import Elasticsearch

class listener(StreamListener):

	s = []
	es = Elasticsearch()
	def on_data(self, raw_data):
		#self.es.index(index="data", doc_type="tweets", body=raw_data)

		json_data = json.loads(raw_data)
		if json_data.get("text", None) is not None:

			co = json_data["coordinates"]
			loc = json_data["user"]["location"]
			text = json_data['text']
			if loc is not None or co is not None:
				self.es.index(index="data", doc_type="tweets", body=raw_data)
				#print (text)
		return True

	def on_error(self, status_code):
		print(status_code)

	def on_disconnect(self, notice):
		print (self.s)



def main():
	c_key = "dw9w6y9O432ndFsBe3Dfu5LR1"
	c_secret = "bremcvPZ7I5WOh9vyHyLOo8R2BNRXKVZ3bfldareVx97kKT1wL"
	a_token = "147592347-gpKOcO2bDcwPI55bUBgjQ2u57qlZjWiowhu9D3H3"
	a_secret = "YJIpb3tuTmMkVq5Qcbhb625whnQJeZagoZrFx82p0jgBi"
	auth = OAuthHandler(c_key, c_secret)
	auth.set_access_token(a_token, a_secret)

	tweets = tweepy.Stream(auth, listener())
	tweets.filter(track=["trump", "hillary", "election2016", "NBA", "diwali"], async=True)


if __name__ == "__main__":
	main()