from app.model.connection import my_db

chapters = my_db['chapters']
books = my_db['books']


def insert_new_book(title, author, rate, info, img_src, url):
    # params as dict
    books.insert_one(locals())


if __name__ == '__main__':
    chapters.delete_one({"book_url": "xiuluo", "href": "http://www.nitianxieshen.com/shengwu/1152.html"})

