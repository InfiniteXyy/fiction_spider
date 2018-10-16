from app.model.connection import my_db

chapters = my_db['chapters']
books = my_db['books']

if __name__ == '__main__':
    chapters.delete_many({"book_url": "xieshen"})
    print(chapters.estimated_document_count())
    # chapters.update_many({}, {"$set": {'book_url': 'jianling'}})

