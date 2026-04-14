from googleapiclient.discovery import build

def get_youtube_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100, # Mengambil 100 komentar teratas
            textFormat="plainText"
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        
        return comments
    except Exception as e:
        print(f"Error: {e}")
        return []