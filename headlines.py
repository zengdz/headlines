#2016/09/26

from flask import Flask
import feedparser

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             '163': 'http://news.163.com/special/00011K6L/rss_newstop.xml',
             'chinadaily': 'http://www.chinadaily.com.cn/rss_c/kjhlw.xml',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication = 'bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
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
    app.run(port=3000, debug=True)
