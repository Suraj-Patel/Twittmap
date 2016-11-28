from elasticsearch import Elasticsearch

def main(json_tweet_data):

	es = Elasticsearch()
	try:

		es.index(index="data", doc_type="tweets", body=json_tweet_data)

	except UnicodeEncodeError as u:
		pass
