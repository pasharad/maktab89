from pymongo import MongoClient


client = MongoClient('localhost', 27017)


db = client.mflix

movies = db.movies.find({'genres':'History'},{'_id':0, 'title':1})
for m in movies:
    print(m)


    



