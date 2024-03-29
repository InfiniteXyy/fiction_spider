import pymongo
from app.model.connection import my_db

chapters = my_db["chapters"]

PAGE_SIZE = 70

if "chapters" not in my_db.list_collection_names():
    print("create collection chapters")
    my_db.create_collection("chapters")


def get_chapters(book_url, page, sort_type):
    page = page - 1
    sort = pymongo.ASCENDING if sort_type == "asc" else pymongo.DESCENDING
    return list(
        chapters.find({"book_url": book_url}, {"content": False}).sort([("index", sort)]).limit(PAGE_SIZE).skip(
            page * PAGE_SIZE))


def get_chapter_by_index(book_url, index):
    result = chapters.find_one({"$and": [{"book_url": book_url}, {"index": index}]})
    return result


def get_chapters_count(book_url):
    return chapters.count_documents({"book_url": book_url})


def get_page_size() -> int:
    return PAGE_SIZE


def get_prev_next_chapter_titles(book_url, index):
    return list(chapters.find({"$and": [{"book_url": book_url}, {"$or": [{"index": index - 1}, {"index": index + 1}]}]},
                              {"_id": False, "content": False, "book": False, "book_url": False, "href": False}))


if __name__ == '__main__':
    print(get_prev_next_chapter_titles("xieshen", 1255))
