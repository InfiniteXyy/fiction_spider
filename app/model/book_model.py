import pymongo
from .connection import my_db

books = my_db["books"]

if "chapters" not in my_db.list_collection_names():
    print("create collection books")
    my_db.create_collection("books")


def get_books():
    return books.find().sort([("update_time", pymongo.DESCENDING)])


def get_book_title_by_url(url):
    return books.find_one({"url": url})["title"]


def get_book_by_url(url):
    return books.find_one({"url": url})
