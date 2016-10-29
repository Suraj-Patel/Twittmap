from flask import Flask, render_template, request
import get_tweets
import search

application = Flask(__name__)

@application.route("/", methods=['GET', 'POST'])
def main():
	get_tweets.main()
	if request.method == "POST":
		tagValue = request.form.get("tags")
		locations = search.search(tagValue)
		return render_template("index.html", locs = locations)
	else:
		return render_template("index.html", locs=[])

if __name__ == "__main__":
	application.run()