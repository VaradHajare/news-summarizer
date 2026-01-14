# News Summarizer

A modern, AI-powered news aggregation and summarization platform that fetches news from multiple trusted sources and provides summaries with citations.

![News Summarizer Screenshot](screenshot.png)

## Features

- **Multi-Source News Aggregation** - Fetches news from trusted sources including BBC, CNN, Reuters, TechCrunch, The Verge, Wired, and more
- **AI-Powered Summarization** - Uses DistilBART model to generate concise summaries of articles
- **Citations** - Summarize any topic with inline citations [1], [2] linking to source articles
- **Modern Dark UI** - Beautiful glassmorphism design with responsive grid layout
- **Article Reader** - Click any article to view full content in a modal popup
- **Dual API Integration** - Uses both NewsAPI and GNews API for comprehensive coverage

## Tech Stack

- **Backend**: Django 4.0+
- **AI/ML**: Hugging Face Transformers (DistilBART)
- **Article Extraction**: Newspaper3k
- **APIs**: NewsAPI, GNews API
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript

## Project Structure

```
news-summarizer/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── newsanalyzer/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── news/                   # Main application
    ├── views.py            # API endpoints & page rendering
    ├── utils.py            # News fetching & AI summarization
    ├── urls.py             # URL routing
    └── templates/
        └── news/
            └── home.html   # Frontend UI
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VaradHajare/news-summarizer.git
   cd news-summarizer
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

5. **Open in Browser**: Navigate to `http://localhost:8000`

## API Keys

The application uses two news APIs:

- **NewsAPI** - Already configured (free tier: 100 requests/day for development)
- **GNews API** - Get your free key at [gnews.io](https://gnews.io) and update `GNEWS_API_KEY` in `news/utils.py`

## Usage

### Browse Headlines
The homepage displays top headlines from trusted news sources in a responsive card grid.

### Search News
Enter a topic in the search bar and click "Search" to find related articles.

### Summarize Topic
Enter a topic and click "Summarize Topic" to get an AI-generated summary combining information from multiple sources, complete with inline citations and a references section.

### Read Articles
Click any article card to view the full article content in a popup modal.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Author

[Varad Hajare](https://github.com/VaradHajare)
