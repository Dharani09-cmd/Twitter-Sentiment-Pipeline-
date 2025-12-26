from flask import Flask, render_template, request, send_file, jsonify
from scraper import scrape_tweets
from preprocess import clean_text
from model import get_sentiment
import pandas as pd
import plotly.express as px
import io

app = Flask(__name__)
latest_df = None

@app.route("/", methods=["GET", "POST"])
def index():
    global latest_df
    chart_json = None
    results = None

    if request.method == "POST":
        query = request.form["query"]
        limit = int(request.form.get("limit", 50))
        lang = request.form.get("lang") or None
        since = request.form.get("since") or None
        until = request.form.get("until") or None

        df = scrape_tweets(query, limit=limit, lang=lang, since=since, until=until)
        df["clean"] = df["tweet"].apply(clean_text)
        df["sentiment"], df["score"] = zip(*df["clean"].apply(get_sentiment))

        latest_df = df.copy()
        results = df.values.tolist()

        # Sentiment counts
        counts = df["sentiment"].value_counts().reset_index()
        counts.columns = ["sentiment", "count"]
        fig = px.pie(counts, names="sentiment", values="count", title="Sentiment Distribution")
        chart_json = fig.to_html(full_html=False)

    return render_template("index.html", results=results, chart=chart_json)

@app.route("/download/csv")
def download_csv():
    global latest_df
    if latest_df is None:
        return "No data yet"
    buf = io.StringIO()
    latest_df.to_csv(buf, index=False)
    buf.seek(0)
    return send_file(
        io.BytesIO(buf.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="sentiment_results.csv",
    )

@app.route("/api/sentiment")
def api_sentiment():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "query required"}), 400
    df = scrape_tweets(query, limit=20)
    df["clean"] = df["tweet"].apply(clean_text)
    df["sentiment"], df["score"] = zip(*df["clean"].apply(get_sentiment))
    return df.to_dict(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)