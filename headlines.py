#2016/09/26
#2016/10/03

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
    first_article = feed['entries'][0]
    return render_template("home.html",
                           title = first_article.get("title"),
                           published=first_article.get("published"),
                           summary=first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=3000, debug=True)
