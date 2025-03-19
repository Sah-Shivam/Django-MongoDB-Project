import pymongo

url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['newapps1']
person_collection = db["person_collection"]