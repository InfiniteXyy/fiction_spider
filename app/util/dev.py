from app.model.connection import my_db
import datetime
import time

chapters = my_db['chapters']
books = my_db['books']

if __name__ == '__main__':
    books.update_one({"url": "xieshen"}, {"$set": {'update_time': time.time()}})
