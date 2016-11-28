from elasticsearch import Elasticsearch

def main(json_tweet_data):

	es = Elasticsearch()
	#print("es")
	#print(json_tweet_data)
	try:

		es.index(index="data", doc_type="tweets", body=json_tweet_data)

	except UnicodeEncodeError as u:
		pass

