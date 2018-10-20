import pymongo
from app.model.connection import my_db

subscribe = my_db["subscribe"]
if "subscribe" not in my_db.list_collection_names():
    print("没有订阅信息表,创建订阅")
    my_db.create_collection("subscribe")


def addSubscibeToDB(book, name):
    insert = {}
    insert['book'] = book
    insert['name'] = name
    lists = list(subscribe.find({"book": book, "name": name}))
    print(lists)
    if len(lists) != 0:
        print("已经订阅")
    else:
        subscribe.insert_one(insert)
if __name__ == '__main__':
    items = list(subscribe.find({"book":"逆天邪神"}))
    for i in items:
        print(i.get("name"))