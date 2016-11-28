from kafka import KafkaConsumer
from watson_developer_cloud import AlchemyLanguageV1
from watson_developer_cloud.watson_developer_cloud_service import WatsonException
import json
from publish_tweet_notification import PublishTweetNotification


def get_sentiment(text):

	alchemy = AlchemyLanguageV1(api_key="b1b9319ebb52ba6330089887c476c20857add87c")
	try:
		json_sentiment = json.loads(json.dumps(alchemy.sentiment(text=text), indent=2))
		sentiment_type = json_sentiment["docSentiment"]["type"]

	except WatsonException as w:
		print(w)
		return "Exception"

	return sentiment_type

def main():

	consumer = KafkaConsumer("Tweets")

	for message in consumer:
		json_tweet_data = message.value.decode("utf-8")
		tweet_data = json.loads(json_tweet_data)
		text = tweet_data["text"]
		sentiment = get_sentiment(text)

		if sentiment != "Exception":
			tweet_data["sentiment"] = sentiment
			json_tweet_data = json.dumps(tweet_data)
			PublishTweetNotification(json_tweet_data)

if __name__ == "__main__":
	main()