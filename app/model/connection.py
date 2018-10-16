import pymongo
# stupid way
with open("../../.env") as f:
    mongo_url = f.read()
my_client = pymongo.MongoClient(mongo_url)
my_db = my_client["internet-novel"]