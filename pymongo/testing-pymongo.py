import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["starwars"]
people = db["people"]
result = people.find_one({"name": "Luke Skywalker"})
print(result)