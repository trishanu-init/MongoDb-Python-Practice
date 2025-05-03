import os
import pprint
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MoONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MoONGODB_URI)

db=client.bank

accounts_collection = db.accounts

document_to_find= {"balance": {"$gt": 10}}

#Find multiple method
cursor=accounts_collection.find(document_to_find)

num_docs=0
for i in cursor:
    num_docs+=1
    pprint.pprint(i)
    print()

print("# of documents found: ", str(num_docs))

client.close()