from youtube_handler import get_youtube_comments
from nlp_processor import clean_text, analyze_sentiment
from database import init_db, load_to_db
import pandas as pd

def run_etl(video_id, api_key):
    print("🚀 Starting ETL Pipeline...")
    
    # 1. EXTRACT
    raw_comments = get_youtube_comments(video_id, api_key)
    if not raw_comments:
        print("❌ Extraction failed.")
        return False

    # 2. TRANSFORM
    processed_data = []
    for comment in raw_comments:
        cleaned = clean_text(comment)
        sentiment = analyze_sentiment(cleaned)
        processed_data.append({
            'original_text': comment,
            'clean_text': cleaned,
            'sentiment': sentiment
        })
    
    df = pd.DataFrame(processed_data)
    
    # 3. LOAD
    init_db()
    load_to_db(df)
    
    print(f"✅ Success! {len(df)} records loaded to Database.")
    return True

if __name__ == "__main__":
    # Test run
    # run_etl('cYOksrJNTGI', 'YOUR_API_KEY')
    pass