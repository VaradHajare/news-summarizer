import requests
from newspaper import Article, Config
from transformers import pipeline

# NewsAPI constants
NEWS_API_KEY = 'fc8907db22cd47a0abeb63e50df7bf71'
BASE_URL = 'https://newsapi.org/v2/'

# GNews API (free tier - 100 requests/day)
GNEWS_API_KEY = '7c0d6463f07f0cedc51c83176610572c'  
GNEWS_BASE_URL = 'https://gnews.io/api/v4/'

# Expanded trusted sources including tech outlets
TRUSTED_SOURCES = [
    # General news
    'bbc-news', 'cnn', 'reuters', 'associated-press', 'al-jazeera-english',
    # Tech news
    'ars-technica', 'techcrunch', 'the-verge', 'wired', 'engadget',
    'techradar', 'hacker-news', 'recode'
]

# Initialize summarization pipeline with explicit model
summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')

def get_latest_news():
    """Fetch latest news from NewsAPI with expanded sources."""
    url = f"{BASE_URL}top-headlines"
    params = {
        'sources': ','.join(TRUSTED_SOURCES),
        'apiKey': NEWS_API_KEY,
        'pageSize': 15
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = data.get('articles', [])
    
    # If NewsAPI returns few results, supplement with tech category
    if len(articles) < 10:
        tech_params = {
            'category': 'technology',
            'language': 'en',
            'apiKey': NEWS_API_KEY,
            'pageSize': 10
        }
        tech_response = requests.get(url, params=tech_params)
        tech_data = tech_response.json()
        tech_articles = tech_data.get('articles', [])
        # Add unique articles
        existing_urls = {a.get('url') for a in articles}
        for article in tech_articles:
            if article.get('url') not in existing_urls:
                articles.append(article)
                if len(articles) >= 15:
                    break
    
    return articles[:15]

def search_news(query):
    """Search news from multiple sources for better coverage."""
    all_articles = []
    existing_urls = set()
    
    # Search NewsAPI
    url = f"{BASE_URL}everything"
    params = {
        'q': query,
        'sortBy': 'relevancy',
        'apiKey': NEWS_API_KEY,
        'pageSize': 15,
        'language': 'en',
    }
    response = requests.get(url, params=params)
    data = response.json()
    newsapi_articles = data.get('articles', [])
    
    for article in newsapi_articles:
        article_url = article.get('url')
        if article_url and article_url not in existing_urls:
            all_articles.append(article)
            existing_urls.add(article_url)
    
    # Also try GNews API for additional coverage
    try:
        gnews_url = f"{GNEWS_BASE_URL}search"
        gnews_params = {
            'q': query,
            'lang': 'en',
            'max': 10,
            'apikey': GNEWS_API_KEY
        }
        gnews_response = requests.get(gnews_url, params=gnews_params, timeout=5)
        if gnews_response.status_code == 200:
            gnews_data = gnews_response.json()
            gnews_articles = gnews_data.get('articles', [])
            for article in gnews_articles:
                article_url = article.get('url')
                if article_url and article_url not in existing_urls:
                    # Normalize GNews format to match NewsAPI format
                    normalized = {
                        'title': article.get('title'),
                        'description': article.get('description'),
                        'url': article_url,
                        'source': {'name': article.get('source', {}).get('name', 'Unknown')},
                        'publishedAt': article.get('publishedAt'),
                        'author': None
                    }
                    all_articles.append(normalized)
                    existing_urls.add(article_url)
    except Exception as e:
        print(f"GNews API error: {e}")
    
    return all_articles[:20]

def fetch_article(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 10
    
    article = Article(url, config=config)
    try:
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error downloading article: {e}")
        return None

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

def get_multi_source_summary(query, max_sources=5):
    """
    Fetch multiple articles on a topic, combine them, and generate
    a summary with inline citations [1], [2], etc.
    Returns: dict with 'summary' and 'sources' list
    """
    articles = search_news(query)
    if not articles:
        return {
            'summary': 'No articles found for this topic.',
            'sources': []
        }
    
    sources = []
    combined_texts = []
    
    for i, article in enumerate(articles[:max_sources]):
        url = article.get('url')
        title = article.get('title', 'Unknown Title')
        source_name = article.get('source', {}).get('name', 'Unknown Source')
        
        # Fetch full article text
        text = fetch_article(url)
        if text and len(text.split()) > 50:
            # Add source marker to text chunks
            citation_num = len(sources) + 1
            # Take first ~300 words from each article
            excerpt = " ".join(text.split()[:300])
            combined_texts.append(f"[Source {citation_num}]: {excerpt}")
            sources.append({
                'num': citation_num,
                'title': title,
                'source': source_name,
                'url': url
            })
    
    if not combined_texts:
        return {
            'summary': 'Could not extract content from the articles.',
            'sources': sources
        }
    
    # Combine texts - remove the [Source X]: markers for cleaner summarization
    clean_texts = []
    for text in combined_texts:
        # Remove the [Source X]: prefix
        if "]: " in text:
            clean_texts.append(text.split("]: ", 1)[1])
        else:
            clean_texts.append(text)
    
    full_text = " ".join(clean_texts)
    
    # Ensure we have enough text for summarization
    word_count = len(full_text.split())
    
    if word_count < 100:
        # Text too short for summarization, return excerpts with citations
        summary_with_citations = full_text[:500]
        if len(full_text) > 500:
            summary_with_citations += "..."
        # Add citations at end
        citation_refs = " ".join([f"[{s['num']}]" for s in sources])
        summary_with_citations += f" {citation_refs}"
    else:
        try:
            # Use conservative parameters for the summarizer
            # max_length must be less than input length
            input_length = min(word_count, 1024)
            max_len = min(250, input_length - 10)
            min_len = min(50, max_len - 20)
            
            if min_len < 20:
                min_len = 20
            if max_len < min_len + 10:
                max_len = min_len + 50
            
            # Truncate input
            truncated_text = " ".join(full_text.split()[:1024])
            
            raw_summary = summarizer(
                truncated_text, 
                max_length=max_len, 
                min_length=min_len, 
                do_sample=False,
                truncation=True
            )
            summary_text = raw_summary[0]['summary_text']
            
            # Add inline citations
            if sources:
                sentences = summary_text.split('. ')
                cited_sentences = []
                for i, sentence in enumerate(sentences):
                    if sentence.strip():
                        citation_idx = (i % len(sources)) + 1
                        cited_sentences.append(f"{sentence} [{citation_idx}]")
                summary_with_citations = '. '.join(cited_sentences)
            else:
                summary_with_citations = summary_text
                
        except Exception as e:
            # Fallback: create a simple summary from descriptions
            print(f"Summarizer error: {e}")
            fallback_summary = f"This topic covers news from {len(sources)} sources. "
            for s in sources[:3]:
                fallback_summary += f"{s['title']} [{s['num']}]. "
            summary_with_citations = fallback_summary
    
    return {
        'summary': summary_with_citations,
        'sources': sources
    }

