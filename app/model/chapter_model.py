import pymongo
from .connection import my_db

chapters = my_db["chapters"]

PAGE_SIZE = 30

if "chapters" not in my_db.list_collection_names():
    print("create collection chapters")
    my_db.create_collection("chapters")


def get_chapters(book_url, page, sort_type):
    page = page - 1
    sort = pymongo.ASCENDING if sort_type == "asc" else pymongo.DESCENDING
    return list(chapters.find({"book_url": book_url}, {"content": False}).sort([("index", sort)]).limit(PAGE_SIZE).skip(
        page * PAGE_SIZE))


def get_chapter_by_index(book_url, index):
    result = chapters.find_one({"$and": [{"book_url": book_url}, {"index": index}]})
    return result


def get_max_page(book_url):
    return chapters.count_documents({"book_url": book_url}) // PAGE_SIZE + 1
