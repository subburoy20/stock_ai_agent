import streamlit as st
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page config
st.set_page_config(page_title="📊 Stock AI Agent", layout="centered")
st.title("📊 Stock AI Agent System (Free)")
st.markdown("Enter stock name like `TCS`, `RELIANCE`, `INFY` to get live Twitter sentiment analysis.")

# Input box
stock = st.text_input("🔍 Enter Stock Name (e.g. RELIANCE, TCS, INFY)")

# Twitter Sentiment Analysis
def twitter_sentiment(stock_name):
    analyzer = SentimentIntensityAnalyzer()
    tweets = []

    # Use snscrape to get last 50 tweets
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{stock_name} stock since:2023-07-01').get_items()):
        if i > 50:
            break
        tweets.append(tweet.content)

    if not tweets:
        return "❌ No tweets found", 0

    # Calculate average compound score
    scores = [analyzer.polarity_scores(t)["compound"] for t in tweets]
    avg_score = sum(scores) / len(scores)
    return "✅ Success", round(avg_score, 3)

# Button action
if st.button("📈 Run Analysis"):
    if stock.strip() == "":
        st.warning("⚠️ Please enter a stock name.")
    else:
        st.info(f"Fetching tweets for: `{stock}`")
        status, sentiment = twitter_sentiment(stock)
        st.write("Status:", status)

        if status == "✅ Success":
            st.metric("📊 Sentiment Score", sentiment)

            if sentiment > 0.05:
                st.success("📈 Positive Sentiment")
            elif sentiment < -0.05:
                st.error("📉 Negative Sentiment")
            else:
                st.warning("⚖️ Neutral Sentiment")
