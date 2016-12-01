from elasticsearch import Elasticsearch

def main(json_tweet_data):

	es = Elasticsearch()

	try:
		es.index(index="data", doc_type="tweets", body=json_tweet_data)
		#print("data added")
	except UnicodeEncodeError as u:
		print(u)
		pass

