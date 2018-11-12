from flask import Blueprint, render_template, Response
from app.model import book_model
from app.model import chapter_model

rss = Blueprint("rss", __name__)


@rss.route("/<string:book_url>.atom")
def get_atom(book_url):
    book = book_model.get_book_by_url(book_url)
    chapters = chapter_model.get_chapters(book_url, 1, "desc")
    chapters.reverse()
    props = {
        "book": book,
        "chapters": chapters,
    }
    rss_xml = render_template('rss.xml', **props)
    return Response(rss_xml, mimetype='text/xml')
