from flask import render_template
from app import app
from .request import get_source

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


  business_source = get_source('business')
  entertainment_source = get_source('entertainment')
  international_source = get_source('international')
  local_source = get_source('local')
  technology_source = get_source('technology')
  health_source = get_source('health')
  weather_source = get_source('weather')
  sport_source = get_source('sport')
  # print(sport_source)
  title = 'News Briefs'
  return render_template('index.html', title = title, sport = sport_source,business = business_source, entertainment = entertainment_source, international = international_source, local = local_source, technology = technology_source, health = health_source, weather = weather_source)


# @app.route('/source/<id>')
# def source(id):
#
#     articles = get_articles(id)
#
#     source_id = id
#     title = f'{source_id}'
#     return render_template('source.html',title = title,article = article)
