
from flask import Flask
import feedparser
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'engadget': 'https://www.engadget.com/rss.xml'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication = 'bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles = feed['entries'])

if __name__ == '__main__':
    app.run(port=3000, debug=True)
