import requests
from newspaper import Article
from transformers import pipeline

# NewsAPI constants
NEWS_API_KEY = 'fc8907db22cd47a0abeb63e50df7bf71'
BASE_URL = 'https://newsapi.org/v2/'

# Initialize summarization pipeline with explicit model
summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')

def get_latest_news():
    url = f"{BASE_URL}top-headlines"
    params = {
        'language': 'en',
        'apiKey': NEWS_API_KEY,
        'pageSize': 10
    }
    response = requests.get(url, params=params)
    print(response.json())  # Debug output
    data = response.json()
    return data.get('articles', [])

def search_news(query):
    url = f"{BASE_URL}everything"
    params = {
        'q': query,
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API_KEY,
        'pageSize': 5,
        'language': 'en',   # Add this line for English-only news
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('articles', [])

def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_text(text):
    max_tokens = 1024
    # Simple token truncation by words (approximate)
    truncated_text = " ".join(text.split()[:max_tokens])
    summary = summarizer(truncated_text, max_length=250, min_length=100, do_sample=False)
    return summary[0]['summary_text']

def get_summarized_news(url):
    text = fetch_article(url)
    if not text or len(text.split()) < 50:
        return "Sorry, the article text is too short or could not be extracted."
    return summarize_text(text)
