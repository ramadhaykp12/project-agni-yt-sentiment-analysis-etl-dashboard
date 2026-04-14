import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Inisialisasi Analis
analyzer = SentimentIntensityAnalyzer()
stopword_factory = StopWordRemoverFactory()
stopword_remover = stopword_factory.create_stop_word_remover()

def clean_text(text):
    # Hapus URL
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Hapus mention dan hashtag
    text = re.sub(r'\@\w+|\#','', text)
    # Hapus karakter non-alphanumeric (tapi simpan emoji dasar)
    text = re.sub(r'[^\w\s\u1f600-\u1f64f]', '', text)
    text = text.lower().strip()
    return text

def analyze_sentiment(text):
    if not text:
        return "Netral"
    
    # VADER sangat efektif untuk bahasa campuran karena mengenali emoji,
    # tanda baca (!!!), dan kata-kata slang Inggris yang sering dipakai netizen Indo
    vs = analyzer.polarity_scores(text)
    score = vs['compound']
    
    if score >= 0.05:
        return "Positif"
    elif score <= -0.05:
        return "Negatif"
    else:
        return "Netral"

def get_wordcloud_text(df):
    all_text = " ".join(df['Clean_Comment'])
    # Hapus stopwords Indonesia
    cleaned = stopword_remover.remove(all_text)
    # Hapus kata-kata umum yang tidak bermakna dalam konteks youtube/game
    extra_stops = {'the', 'and', 'this', 'game', 'video', 'is', 'it', 'to', 'for', 'of', 'in', 'looks'}
    words = [w for w in cleaned.split() if w not in extra_stops and len(w) > 2]
    return " ".join(words)