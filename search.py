from elasticsearch import Elasticsearch
import json

def search(term):
	locations = {}
	es = Elasticsearch()

	res = es.search(index="data", doc_type="tweets", body={"query": {"query_string": {"query": term}}})
	for doc in res['hits']['hits']:
		sentiment = doc['_source']['sentiment']
		#print(" %s" % (sentiment))
		loc = doc['_source']['coordinates']['coordinates']

		#swap values of coordinates to plot on map
		temp = loc[0]
		loc[0] = loc[1]
		loc[1] = temp

		locations[str(loc)] = sentiment

	print(locations)
	return locations

if __name__ == "__main__":
	print(len(search("instagram").items()))
