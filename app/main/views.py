from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business_source = get_source('business')
    entertainment_source = get_source('entertainment')
    general_source = get_source('general')
    health_source = get_source('health')
    science_source = get_source('science')
    sports_source = get_source('sports')
    technology_source = get_source('technology')

    title = 'News Briefs'
    return render_template('index.html', title = title,business = business_source, entertainment = entertainment_source, general = general_source, health = health_source, science = science_source, sports = sports_source, technology = technology_source)


@main.route('/source/<id>')
def source(id):

    articles = get_articles(id)

    source_id = id
    title = f'{source_id}'
    return render_template('source.html',title = title,article = article)
