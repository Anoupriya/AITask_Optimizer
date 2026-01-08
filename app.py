import streamlit as st
from textblob import TextBlob
import pandas as pd

st.set_page_config(page_title="Amdox AI Task Optimizer", layout="centered")

st.title("AI-Powered Task Optimizer")
text = st.text_area("Enter message")

def analyze_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3:
        return "Happy 😊", "Creative / Challenging Tasks", polarity
    elif polarity < -0.3:
        return "Stressed 😟", "Light or Supportive Tasks", polarity
    else:
        return "Neutral 😐", "Routine Tasks", polarity

if st.button("Analyze Mood"):
    if text.strip():
        mood, task, polarity = analyze_emotion(text)

        st.subheader("Analysis Results")
        col1, col2 = st.columns(2)
        col1.metric("Detected Mood", mood)
        col2.metric("Sentiment Score", round(polarity, 2))

        st.info(f"Recommended Task: **{task}**")

        if "Stressed" in mood:
            st.warning("HR Alert: Prolonged stress detected")

        st.subheader(" Sentiment Polarity Analysis")
        polarity_df = pd.DataFrame({
            "Metric": ["Sentiment Polarity"],
            "Score": [polarity]
        })
        st.bar_chart(polarity_df.set_index("Metric"))

        st.subheader("Team Mood Distribution (Sample Data)")
        mood_data = pd.DataFrame({
            "Mood": ["Happy", "Neutral", "Stressed"],
            "Count": [6, 3, 2]
        })
        st.line_chart(mood_data.set_index("Mood"))

    else:
        st.error("Please enter some text")
