from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

MAPPING = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

def get_sentiment(text):
    result = sentiment_model(text)[0]
    sentiment = result["label"]
    score = float(result["score"])
    return MAPPING.get(sentiment, "Unknown"), round(score, 3)