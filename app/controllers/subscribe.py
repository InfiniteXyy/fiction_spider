from flask import Blueprint, request, Response
from app.model import subscribe_model
from app.model import book_model
import json

subscribe = Blueprint("subscribe", __name__)


@subscribe.route("/")
def subscribe_book():
    nickname = request.args.get("nickname", type=str)
    book_url = request.args.get("book_url", type=str)
    if book_url == "" or nickname == "":
        return "args wrong"
    if not book_model.get_book_by_url(book_url):
        return "book url not exist"
    result = subscribe_model.add_subscribe(book_url, nickname)
    if result:
        return "success"
    else:
        return "has already subscribed"


@subscribe.route("/booksub")
def get_subscribe_by_book():
    book_url = request.args.get("book_url", type=str)
    users = list(subscribe_model.get_subscribe_list_by_book(book_url))
    result = {"code": 200, "users": users}
    return Response(json.dumps(result), mimetype='application/json')


@subscribe.route("/usersub")
def get_subscribe_by_nickname():
    nickname = request.args.get("nickname", type=str)
    books = list(subscribe_model.get_subscribe_list_by_nickname(nickname))
    result = {"code": 200, "books": books}
    return Response(json.dumps(result), mimetype='application/json')
