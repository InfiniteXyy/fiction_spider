from flask import Flask
from app.controllers.main import main
from app.controllers.subscribe import subscribe
from app.controllers.rss import rss
from app.model import book_model
from app.model import chapter_model
from flask_bootstrap import Bootstrap
from datetime import datetime
from app.util.page_helper import create_page_index

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(rss, url_prefix='/rss')
# app.register_blueprint(subscribe, url_prefix='/sub')


def format_datetime(value, time_format='datetime'):
    if not value:
        return "无"
    if time_format == 'date':
        time_format = "%m月%d日"
    elif time_format == 'datetime':
        time_format = "%m月%d日"
    return datetime.utcfromtimestamp(value).strftime(time_format)


def format_article_content(value):
    lines = value.split("\n")
    lines = filter(lambda x: x.strip() != '', lines)
    return lines


app.jinja_env.filters['datetime'] = format_datetime
app.jinja_env.filters['article'] = format_article_content
