from elasticsearch import Elasticsearch
import json

def search(term):
	locations = {}
	es = Elasticsearch()
	query = json.dumps({
		"query": {
			"match": {
				"text": term
			}
		}
	})
	res = es.search(index="data", doc_type="tweets", body=query)
	for doc in res['hits']['hits']:
		sentiment = doc['_source']['sentiment']
		print(" %s" % (sentiment))
		loc = doc['_source']['location']
		print(" %s" % (loc))

		locations[loc] = sentiment

	return locations

if __name__ == "__main__":
	search("trump")