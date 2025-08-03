import streamlit as st
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(page_title="📊 Stock AI Agent", layout="centered")
st.title("📊 Stock AI Agent System (Free)")
st.markdown("Enter stock symbol like `TCS`, `RELIANCE` to get analysis.")

stock = st.text_input("Enter Stock Symbol (Example: TCS)")

# 🐦 Twitter Sentiment Function
def twitter_sentiment(stock_name):
    analyzer = SentimentIntensityAnalyzer()
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"{stock_name} stock since:2023-07-01").get_items()):
        if i > 50: break
        tweets.append(tweet.content)

    scores = [analyzer.polarity_scores(t)["compound"] for t in tweets]
    avg_score = sum(scores) / len(scores) if scores else 0
    return round(avg_score, 2)

# 🔍 When Button is Clicked
if st.button("Run Analysis"):
    st.success(f"Running Twitter Sentiment Analysis for {stock}...")

    sentiment_score = twitter_sentiment(stock)
    
    if sentiment_score > 0:
        st.markdown(f"📈 **Positive Sentiment Score:** `{sentiment_score}`")
    elif sentiment_score < 0:
        st.markdown(f"📉 **Negative Sentiment Score:** `{sentiment_score}`")
    else:
        st.markdown(f"⚖️ **Neutral Sentiment Score:** `{sentiment_score}`")
