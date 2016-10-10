
import json
import urllib2
import urllib 
import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'engadget': 'https://www.engadget.com/rss.xml'}

def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ffbf9455a5a14c28bef75a03a8a7b308"#appid=a private API KEY
    query = urllib.quote(query)#replace space in city's name with %20,url can't have space
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":parsed["weather"][0]["description"],
                    "temperature":parsed["main"]["temp"],"city":parsed["name"]}
    return weather

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    weather = get_weather("London,UK")
    return render_template("home.html", articles = feed['entries'], weather=weather)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
