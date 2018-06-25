from app import app
import urllib.request,json
from .models import source

Source = source.Source

#Getting api_key
api_key = app.config['SOURCE_API_KEY']
print(api_key)
#Getting source base url
base_url = app.config['SOURCE_API_BASE_URL']


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
