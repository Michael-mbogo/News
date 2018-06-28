import urllib.request,json
from .models import News,Articles



api_key = None
headlines_url = None
source_url = None
everything_url = None
articles_url = None

def configure_request(app):
    global api_key,headlines_url,everything_url,source_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    print(api_key)
    articles_url = app.config['NEWS_HEADLINES_URL']
    source_url = app.config['NEWS_SOURCE_URL']
    everything_url = app.config['NEWS_EVERYTHING']


def get_news(source):
    get_news_url = source_url.format(source,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_list):
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        news_object = News(name,description,url,category,language,country)
        news_results.append(news_object)
    return news_results



def get_articles(sources):
    sources = sources.replace(" ","+")
    get_articles_url = everything_url.format(sources, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = []

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_resultss(articles_results_list)
    return articles_results

def process_resultss(articles_list):
    articles_results = []
    for articles_item in articles_list:
        name = articles_item.get('source.name')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        articles_object = Articles(name,author,title,description,url,urlToImage,publishedAt)
        articles_results.append(articles_object)
    return articles_results
