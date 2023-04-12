from pymongo import MongoClient

client = MongoClient('localhost', 27017)


db = client.mflix

m = db.movies.aggregate([{'$unwind':"$languages"}, { '$group': { '_id': "$languages", 'average': { '$avg': '$imdb.rating' } } }, {'$sort': {'average':1}}])
for i in m:
    print(i)