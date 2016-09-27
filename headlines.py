#2016/09/26

from flask import Flask
import feedparser

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return """<html>
    <body>
    <h1> BBC Headlines </h1>
    <b>{0}</b> <br/>
    <i>{1}</i> <br/>
    <p>{2}</p> <br/>
    </body>
    </html>""".format(first_article.get("title"), first_article.
    get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
