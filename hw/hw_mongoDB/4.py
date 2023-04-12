from pymongo import MongoClient

client = MongoClient('localhost', 27017)


db = client.mflix


result = db.movies.aggregate([{'$unwind':"$languages"}, { '$group': { '_id': "$languages", 'count': { '$sum': 1 } } }])
for r in result:
    print(r)