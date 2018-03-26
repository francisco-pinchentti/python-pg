# Connects to a mongodb using a MongoDBURI
# taken from os.env
# @see http://api.mongodb.com/python/2.7rc0/tutorial.html

from pymongo import MongoClient
from bson.objectid import ObjectId

import os

CONN_STR = os.getenv('CONN_STR')

client = MongoClient(CONN_STR)

db = client.viorecdm

TESTS = db['TEST']
t_id = TESTS.insert({
	"name": "pepe",
	"at": "De Moon"
})

for t in TESTS.find():
	print t

print t_id
print ObjectId(t_id)
