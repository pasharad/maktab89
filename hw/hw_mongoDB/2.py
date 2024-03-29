from pymongo import MongoClient


client = MongoClient('localhost', 27017)


db = client.mflix

historical_movies = db.movies.aggregate([
{
'$match': {
'$and': [
{'year':{'$type': 'int'}},
{ '$expr': { '$gt': [ 'year', 1990 ] } },
]
},
},
{'$project':{'_id':0, 'title':1, 'year':1}}
])


for i in historical_movies:
    print(i)