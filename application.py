from flask import Flask, render_template, request
import get_tweets
from elasticsearch import Elasticsearch
import add_to_elasticsearch
import search
import boto3
import ast

application = Flask(__name__)


@application.route("/", methods=['GET', 'POST'])
def main():
	get_tweets.main()

	if request.method == "POST":
		tagValue = request.form.get("tags")
		locations = search.search(tagValue)
		return render_template("index.html", locs=locations)
	else:
		return render_template("index.html", locs=[])


@application.route("/notification", methods=['GET', 'POST'])
def receive_notification():
	if request.method == "POST":

		data = request.data
		data = data.decode("utf-8")
		data = ast.literal_eval(data)

		client = boto3.client('sns')

		if data["Type"] == "SubscriptionConfirmation":
			sns_confirm = client.confirm_subscription(
				TopicArn=data["TopicArn"],
				Token=data["Token"],
			)

		else:
			if data["Type"] == "Notification":
				json_tweet_data = data["Message"]
				print("Message Received")
				#json_tweet_data = ast.literal_eval(json_tweet_data)
				add_to_elasticsearch.main(json_tweet_data)
				#print(json_tweet_data)

		return "Hello!"

if __name__ == "__main__":
	application.run()
