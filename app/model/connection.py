import pymongo
from settings import _mongo_url

my_client = pymongo.MongoClient(_mongo_url)
my_db = my_client["internet-novel"]
