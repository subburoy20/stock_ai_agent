import streamlit as st
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(page_title="📊 Stock AI Agent", layout="centered")
st.title("📊 Stock AI Agent System (Free)")
st.markdown("This app analyzes stock sentiment using Twitter. Works 100% free, no API key needed.")

# Input Section
stock = st.text_input("Enter Stock Symbol (Example: TCS, RELIANCE, INFY)")

# 🐦 Twitter Sentiment Agent Function
def twitter_sentiment(stock_name):
    analyzer = SentimentIntensityAnalyzer()
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"{stock_name} stock since:2023-07-01").get_items()):
        if i > 50:
            break
        tweets.append(tweet.content)

    if not tweets:
        return "No tweets found", 0

    # Analyze each tweet
    scores = [analyzer.polarity_scores(t)["compound"] for t in tweets]
    avg_score = sum(scores) / len(scores)
    return "✅ Success", round(avg_score, 2)

# Button to Run Analysis
if st.button("Run Analysis"):
    if stock.strip() == "":
        st.warning("⚠️ Please enter a valid stock name.")
    else:
        st.info(f"🔍 Searching tweets for: {stock}...")
        status, sentiment_score = twitter_sentiment(stock)

        if status == "No tweets found":
            st.error("❌ No tweets found. Try another stock.")
        else:
            st.success(f"✅ Twitter Sentiment Score: {sentiment_score}")
            if sentiment_score > 0.05:
                st.markdown("📈 **Overall: Positive Sentiment**")
            elif sentiment_score < -0.05:
                st.markdown("📉 **Overall: Negative Sentiment**")
            else:
                st.markdown("⚖️ **Overall: Neutral Sentiment**")
