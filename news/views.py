from django.shortcuts import render
from .utils import get_latest_news, search_news, get_summarized_news, fetch_article, get_multi_source_summary
from django.http import JsonResponse

def fetch_full_article(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'No URL provided'}, status=400)
    try:
        content = fetch_article(url)
        if content:
            return JsonResponse({'content': content})
        else:
            return JsonResponse({'error': 'Could not extract article content'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def summarize_topic(request):
    """Generate a multi-source summary with citations for a topic."""
    query = request.GET.get('query')
    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)
    
    result = get_multi_source_summary(query)
    return JsonResponse(result)

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
