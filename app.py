from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    tweet = request.form['tweet'].strip().lower()
    positive_words = ["good", "great", "happy", "love", "excellent", "wonderful"]
    negative_words = ["bad", "sad", "hate", "terrible", "awful", "angry"]

    if not tweet:
        sentiment = "⚠️ Please enter a tweet!"
    elif any(word in tweet for word in positive_words):
        sentiment = "😊 Positive"
    elif any(word in tweet for word in negative_words):
        sentiment = "😞 Negative"
    else:
        sentiment = "😐 Neutral"

    return render_template('index.html', tweet=tweet, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
