from elasticsearch import Elasticsearch
import json

def search(term):
	locations = []
	es = Elasticsearch()
	query = json.dumps({
		"query": {
			"match": {
				"text": term
			}
		}
	})
	res = es.search(index="data", doc_type="tweets", body=query)
	#print("%d documents found" % res['hits']['total'])
	for doc in res['hits']['hits']:
		co = doc['_source']['coordinates']
		loc = doc['_source']['user']['location']
		if co is not None:
			print(" %s" % (co))
			locations.append()
		elif loc is not None:
			print(" %s" % (loc))
			locations.append(loc)

	return locations

if __name__ == "__main__":
	search("#")