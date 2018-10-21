from app.model.connection import my_db

subscribe = my_db["subscribe"]
if "subscribe" not in my_db.list_collection_names():
    print("没有订阅信息表,创建订阅")
    my_db.create_collection("subscribe")


def add_subscribe(book_url, nickname):
    insert = {'book_url': book_url, 'nickname': nickname}
    if len(list(subscribe.find({"book_url": book_url, "nickname": nickname}))) == 0:
        subscribe.insert_one(insert)
        return True
    return False


def get_subscribe_list_by_nickname(nickname):
    return subscribe.find({"nickname": nickname}, {"_id": False})


def get_subscribe_list_by_book(book_url):
    return subscribe.find({"book_url": book_url}, {"_id": False})
