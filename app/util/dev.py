from app.model.connection import my_db

chapters = my_db['chapters']
books = my_db['books']


def insert_new_book(title, author, rate, info, img_src, url):
    # params as dict
    books.insert_one(locals())


if __name__ == '__main__':
    cur_documents = list(chapters.find({"book_url": "jianling"}, {"href": True}))
    href_list = [x['href'] for x in cur_documents]
    print(href_list[0])

