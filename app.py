import streamlit as st

st.set_page_config(page_title="📊 Stock AI Agent", layout="centered")
st.title("📊 Stock AI Agent System (Free)")
st.markdown("Enter stock symbol like `TCS`, `RELIANCE` to get analysis.")

stock = st.text_input("Enter Stock Symbol (Example: TCS)")

if st.button("Run Analysis"):
    st.success(f"Analysis for {stock} will appear here...")
    # You’ll add code later (next steps)
