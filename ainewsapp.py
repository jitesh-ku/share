from flask import Flask, render_template, request
import feedparser
import html

app = Flask(__name__)

rss_feeds = {
    "MIT Technology": "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
    "CNET News": "https://www.cnet.com/rss/news/",
    "Google News": "https://news.google.com/rss/search?q=technology",
    "TechCrunch": "https://techcrunch.com/feed/"
}

def fetch_articles(selected_sources):
    articles = {}
    for source in selected_sources:
        feed = feedparser.parse(rss_feeds[source])
        articles[source] = feed.entries[:5]
    return articles

@app.route("/", methods=["GET", "POST"])
def index():
    summaries = {}

    if request.method == "POST":
        selected_sources = request.form.getlist("sources")
        articles = fetch_articles(selected_sources)

        for source in selected_sources:
            summaries[source] = {}
            for entry in articles[source]:
                key = f"summary_{source}_{entry.link}"
                if request.form.get(key):
                    #summaries[source][entry.link] = "AI Generated Summary Dummy for " + entry.title
                    summaries[source][entry.link] = "AI Generated Summary Dummy for " + html.unescape(entry.summary)

    else:
        selected_sources = list(rss_feeds.keys())
        articles = fetch_articles(selected_sources)

    return render_template("index.html",
                           rss_feeds=rss_feeds,
                           selected_sources=selected_sources,
                           articles=articles,
                           summaries=summaries)

if __name__ == "__main__":
    app.run(debug=True)
