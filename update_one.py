import os
import pprint
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId

load_dotenv()
MoONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MoONGODB_URI)

db=client.bank

accounts_collection = db.accounts

#Update One method
document_to_update={"_id":ObjectId("681614df6b317cdbbe556feb")}

add_to_balance= {"$inc": {"balance": 77000}}

pprint.pprint(accounts_collection.find_one(document_to_update))

result=accounts_collection.update_one(document_to_update, add_to_balance)
print("Document updated: ", str(result.modified_count))

pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()