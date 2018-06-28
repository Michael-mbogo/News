from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_articles
import json

#views
@main.route('/')
def index():
    # Getting news sources
    news_sources = get_news("General")
    #getting articles

    title = 'Home - Welcome to the Greatest News Articles and Everything News Related Website Online'
    return render_template('index.html', title = title,sources = news_sources)

@main.route('/news/<name>')
def news(name):
    articles = get_articles(name)
    return render_template('news.html', articles = articles)
