from django.shortcuts import render
from .utils import get_latest_news, search_news, get_summarized_news
from django.http import JsonResponse
from newspaper import Article

def fetch_full_article(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'No URL provided'}, status=400)
    try:
        article = Article(url)
        article.download()
        article.parse()
        return JsonResponse({'content': article.text})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def home(request):
    url = request.GET.get('url')
    query = request.GET.get('query')
    articles = []
    summary = None

    if url:
        summary = get_summarized_news(url)
    elif query:
        articles = search_news(query)
    else:
        articles = get_latest_news()

    return render(request, 'news/home.html', {
        'articles': articles,
        'summary': summary,
        'query': query,
    })
