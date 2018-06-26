import urllib.request,json
from .models import Source,Article



#Getting api_key
api_key = None
print(api_key)
#Getting source base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']


def get_source(category):
  """
  This function gets json response to our url request
  """
  get_source_url = base_url.format(category,api_key)
  print(get_source_url)
  with urllib.request.urlopen(get_source_url) as url:
      get_source_data = url.read()
      get_source_response = json.loads(get_source_data)
      print(get_source_response)
      source_results = None

      if get_source_response['sources']:
          source_result_list = get_source_response['sources']
          source_results = process_results(source_result_list)

  return source_results

def process_results(source_list):
    """
    function processes the news source results and transform them to a list of objects
    """
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')


        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results

def get_article(title):
    '''
    function that gets the json response to url request
    '''
    get_article_url = article_url.format(title,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_result_list = get_source_response['articles']
            article_results = process_results(article_result_list)

    return article_results

def process_results(article_list):
    '''

    '''
    article_results = []

    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        article_object = Article(author,title,description,url,urlToImage,publishedAt)
        article_results.append(article_object)

    return article_results
