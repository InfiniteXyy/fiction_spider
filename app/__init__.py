from flask import Flask, render_template, request
import app.model.chapter_model as chapter_model
import app.model.book_model as book_model
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)


def format_datetime(value, format='medium'):
    if not value:
        return "无"
    if format == 'full':
        format = "%m月%d日"
    elif format == 'medium':
        format = "%m月%d日"
    return datetime.utcfromtimestamp(value).strftime(format)


app.jinja_env.filters['datetime'] = format_datetime


@app.route("/")
def main():
    books = book_model.get_books()
    return render_template("index.html", books=books)


@app.route("/<string:book_url>")
def chapter_list(book_url):
    page = request.args.get("page", default=1, type=int)
    sort_type = request.args.get("sort", default="asc", type=str)
    next_sort_type = "desc" if sort_type == "asc" else "asc"
    chapters = chapter_model.get_chapters(book_url, page, sort_type)
    if len(chapters) == 0:
        return render_template("404.html")
    max_page = chapter_model.get_max_page(book_url)
    book = book_model.get_book_by_url(book_url)

    props = {
        "chapters": chapters,
        "max_page": max_page,
        "book": book,
        "change_sort_type": next_sort_type
    }

    return render_template("chapter_list.html", **props)


@app.route("/<string:book_url>/articles/<int:index>")
def article(book_url, index):
    chapter = chapter_model.get_chapter_by_index(book_url, index)
    lines = chapter["content"].split("\n")
    lines = filter(lambda x: x.strip() != '', lines)
    props = {"title": chapter["title"],
             "lines": lines, "index": index,
             "next": {"title": "", "href": ""},
             "prev": {"title": "", "href": ""}}

    return render_template("article.html", **props)
