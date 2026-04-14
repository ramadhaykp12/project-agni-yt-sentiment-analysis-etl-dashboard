import streamlit as st
import plotly.express as px
from database import init_db, fetch_data
from etl_pipeline import run_etl
from nlp_processor import get_wordcloud_text
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Agni ETL Dashboard", layout="wide")

st.title("Sentiment Analysis of Agni Village of Calamity based on YouTube Comments")

# --- SIDEBAR CONTROL ---
st.sidebar.header("Pipeline Control")
api_key = st.sidebar.text_input("YouTube API Key", type="password")
video_id = "cYOksrJNTGI"

if st.sidebar.button("Run ETL Pipeline"):
    if api_key:
        with st.spinner("Executing ETL..."):
            success = run_etl(video_id, api_key)
            if success: st.sidebar.success("Pipeline executed!")
    else:
        st.sidebar.warning("API Key required.")

# --- DATA VIEW ---
init_db()
df = fetch_data()

if not df.empty:
    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Records in DB", len(df))
    c2.metric("Latest Sentiment", df['sentiment'].iloc[0])
    c3.metric("Last Update", str(df['extracted_at'].iloc[0]))

    # Visuals
    col_a, col_b = st.columns(2)
    with col_a:
        fig = px.pie(df, names='sentiment', hole=0.4, title="Overall Sentiment Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col_b:
        # Wordcloud menggunakan kolom clean_text dari DB
        text_cloud = " ".join(df['clean_text'].astype(str))
        if text_cloud:
            wc = WordCloud(width=600, height=300, background_color='black').generate(text_cloud)
            fig_wc, ax = plt.subplots()
            ax.imshow(wc)
            ax.axis('off')
            st.pyplot(fig_wc)

    st.write("### Database Preview (Last 100 entries)")
    st.dataframe(df.head(100), use_container_width=True)
else:
    st.info("Database is empty. Please run the ETL Pipeline from the sidebar.")