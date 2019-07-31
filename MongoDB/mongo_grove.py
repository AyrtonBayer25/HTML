# Dependencies
import pymongo
import datetime
# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Declare the database
db = client.fruits_db
# Declare the collection
collection = db.fruits_db
# Part I
# A dictionary that represents the document to be inserted
post = {
    'vendor': 'fruit star',
    'fruit': 'raspberry',
    'quantity': 21,
    'ripeness': 2,
    'date': datetime.datetime.utcnow()
}
# Insert the document into the database
# The database and collection, if they don't already exist, will be created at this point.
collection.insert_one(post)

vendor = input("Vendor name: ")
fruit_type = input("Type of fruit: ")
quantity = input("Number of boxes received: ")
ripeness = input("Ripeness of fruit (1 is unripe; 2 is ripe, 3 is over-ripe: ")

post = {
    'vendor': vendor,
    'fruit': fruit_type,
    'quantity': quantity,
    'ripeness': ripeness,
    'date': datetime.datetime.utcnow()
}

collection.insert_one(post)

results =db.fruits_db.find()
for result in results:
    print(result)
