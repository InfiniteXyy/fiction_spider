from flask import render_template, request, Blueprint
from app.model import book_model
from app.model import chapter_model
from app.util.page_helper import create_page_index

main = Blueprint("main", __name__)


@main.route("/")
def index():
    book_list = book_model.get_books()
    return render_template("index.html", books=book_list)


@main.route("/<string:book_url>")
def chapter_list(book_url):
    page = request.args.get("page", default=1, type=int)
    sort_type = request.args.get("sort", default="asc", type=str)
    next_sort_type = "desc" if sort_type == "asc" else "asc"
    chapters = chapter_model.get_chapters(book_url, page, sort_type)

    if len(chapters) == 0:
        return render_template("404.html")
    chapters_count = chapter_model.get_chapters_count(book_url)
    book = book_model.get_book_by_url(book_url)

    props = {
        "chapters": chapters,
        "chapters_count": chapters_count,
        "pages": create_page_index(chapters_count, chapter_model.get_page_size(), sort_type),
        "cur_page": page,
        "book": book,
        "change_sort_type": next_sort_type,
    }

    return render_template("chapter_list.html", **props)


@main.route("/<string:book_url>/articles/<int:book_index>")
def article(book_url, book_index):
    chapter = chapter_model.get_chapter_by_index(book_url, book_index)
    prev_next = chapter_model.get_prev_next_chapter_titles(book_url, book_index)
    if len(prev_next) == 2:
        prev_next.sort(key=lambda x: x['index'], reverse=True)
        _next = prev_next[0]
        _prev = prev_next[1]
    else:
        if prev_next[0]['index'] < book_index:
            _next = None
            _prev = prev_next[0]
        else:
            _prev = None
            _next = prev_next[0]
    props = {"chapter": chapter,
             "index": book_index,
             "next": _next,
             "prev": _prev}

    return render_template("article.html", **props)
