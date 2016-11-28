import boto3


class PublishTweetNotification:

	def __init__(self, json_tweet_data):

		self.client = boto3.client('sns')
		response = self.client.create_topic(Name="Processed_Tweets")
		self.topic_arn = response['TopicArn']

		subscriber = self.client.subscribe(
			TopicArn=self.topic_arn,
			Protocol='http',
			Endpoint='http://3e57f7c0.ngrok.io/notification'
		)

		self.publish_notification(json_tweet_data)

	def publish_notification(self, data):

		response = self.client.publish(
			TopicArn=self.topic_arn,
			Message=data,
			MessageStructure='string'
		)

		print("Notification Published")
