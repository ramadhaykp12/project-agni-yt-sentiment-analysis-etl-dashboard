# End-to-End Sentiment Data Pipeline & Dashboard of Agni Village of Calamity Game Trailer

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)
![NLP](https://img.shields.io/badge/NLP-Bilingual-green?style=for-the-badge)

An end-to-end **Data Engineering** system designed to scrape, process, and visualize audience sentiment for the Indonesian horror game trailer, **"Agni: Village of Calamity"** (featured on IGN). This project implements a robust ETL pipeline capable of handling bilingual (Indonesian & English) social media data.

## 🚀 Key Features
- **Automated ETL Pipeline**: A seamless workflow covering Data Extraction (YouTube API), Transformation (NLP), and Loading (SQLite).
- **Bilingual Sentiment Analysis**: Integrated **VADER Sentiment** optimized for "code-switching" (mixed Indo-English), slang, and emojis.
- **Persistent Storage**: Uses a local SQL database to store historical comments, preventing data loss and enabling time-series analysis.
- **Interactive Analytics Dashboard**: A real-time UI built with Streamlit featuring sentiment distribution, keyword extraction (WordCloud), and data summaries.

## 🏗️ System Architecture
The project follows a modular architecture:
1. **Extract**: Fetches public comments via the YouTube Data API v3.
2. **Transform**: 
   - Text preprocessing (Regex-based cleaning, Indonesian Stopword removal).
   - Language detection using `langdetect`.
   - Sentiment polarity scoring.
3. **Load**: Ingests enriched data into a `project_agni.db` SQLite database.

## 📊 Data Insights (Sample Findings)
Based on current analysis of 200+ records:
- **Observation Mode**: 61% Neutral sentiment suggests the audience is highly analytical, focusing on technical details rather than just hype.
- **Global Benchmarking**: Keywords like *"Silent Hill"*, *"Joko Anwar"*, and *"Japan"* show that viewers equate the game's quality with world-class horror standards.
- **Audio Appreciation**: "Music" and "Lagu" are dominant topics, indicating that sound design is a primary driver of engagement.

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/yourusername/project-agni-sentiment.git](https://github.com/yourusername/project-agni-sentiment.git)
   cd project-agni-sentiment
   ```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. API Configuration
   - Obtain a YouTube API Key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Input your key in the Streamlit sidebar upon running the application.
4. Run the Dashboard
   ```bash
   streamlit run app.py
   ```
