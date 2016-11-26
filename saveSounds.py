from pymongo import MongoClient

mongoUrl = "mongodb://127.0.0.1:27017/sqwaks"

client = MongoClient(mongoUrl)
db = client["sqwaks"]

cursor = db.sounds.find()

for document in cursor:
    print(document['fileName'])


