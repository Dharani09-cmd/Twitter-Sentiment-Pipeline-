# Twitter Sentiment Pipeline

Welcome to the **Twitter Sentiment Pipeline** project repository! 🌟

## Overview

This project uses **Natural Language Processing (NLP)** and the **Twitter API** to analyze and interpret human sentiments expressed on social media. By fetching and analyzing live tweets, it determines whether a tweet carries a positive, negative, or neutral emotional tone.

It demonstrates the practical application of **AI and sentiment analysis** in understanding public opinions in real time.

---

## Dataset

This project uses **custom live Twitter data** collected via the Twitter API instead of pre-existing datasets. Tweets are fetched dynamically based on keywords, hashtags, or user handles, allowing real-time analysis of trending topics.

---

## Key Steps

**1. Data Collection:**

* Tweets are retrieved using the Twitter API with proper authentication and search filters.

**2. Data Cleaning:**

* Remove URLs, mentions, special characters, and emojis.
* Convert text to lowercase and handle missing or duplicate data.

**3. Text Preprocessing:**

* Tokenization and stopword removal.
* Stemming and lemmatization for better word representation.

**4. Sentiment Analysis:**

* Use **TextBlob** or **VADER Sentiment Analyzer** to calculate sentiment polarity.
* Categorize tweets as *Positive*, *Negative*, or *Neutral*.

**5. Model Deployment:**

* Deployed using **Flask** on **Render Cloud Platform** for live interaction.

---

## How to Use

### 1️⃣ Prerequisites

* **Python 3.9+**

* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

* **Twitter API Key Setup:**

  * Sign up on the [Twitter Developer Platform](https://developer.twitter.com/)
  * Create a new App and get your **Bearer Token**
  * Store it securely in your environment variables before running the app.

---

### 2️⃣ Run the Application

```bash
python app.py
```

Then open your browser and go to:
👉 `http://127.0.0.1:8080`

Enter a tweet or keyword to analyze live sentiment results.

---

### 3️⃣ Deployment on Render

* Push your project to GitHub
* Go to [Render.com](https://render.com)
* Create a **new Web Service**
* Set the **Start Command** as:

  ```
  gunicorn app:app
  ```
* Deploy 🚀

---

## 🧠 Tech Stack

* **Python 3.9+**
* **Flask** (Web Framework)
* **TextBlob / VADER** (Sentiment Analysis)
* **Twitter API v2** (Live Data Source)
* **Gunicorn** (WSGI server for deployment)
* **Render Cloud** (Hosting platform)

---

## 👩‍💻 Author

**Dharani Priya G**
📧 Email: [dharanisuresh555@gmail.com](mailto:dharanisuresh555@gmail.com)

---

## 🚀 Future Enhancements

* Add support for multilingual sentiment analysis
* Visualize sentiment trends using real-time dashboards
* Integrate advanced models like BERT or RoBERTa

---

## 🪪 License

This repository is licensed under the **MIT License** — feel free to use, modify, and distribute the code for educational or research purposes.

---

## ❤️ Acknowledgements

* [Twitter API Documentation](https://developer.twitter.com/en/docs)
* [TextBlob Documentation](https://textblob.readthedocs.io/)
* [Flask Official Docs](https://flask.palletsprojects.com/)
* [Render Deployment Guide](https://render.com/docs/deploy-flask)
