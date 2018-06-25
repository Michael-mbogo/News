from app import app
import urllib.request,json
from .models import source

Source = source.Source

#Getting api_key
api_key = app.config['SOURCE_API_KEY']

#Getting source base url
base_url = app.config['SOURCE_API_BASE_URL']


def get_source(category):
  """
  This function gets json response to our url request
  """
  get_source_url = news_source_url.format(category)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = None

    if get_source_response['sources']:
      source_result_list =get_source_response['sources']

      source_results = process_results(source_result_list)

  return source_results
