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

document_to_delete={"_id":ObjectId("681614df6b317cdbbe556feb")}

#Delete one method
print("Searching for document to delete:")
pprint.pprint(accounts_collection.find_one(document_to_delete))

result=accounts_collection.delete_one(document_to_delete)

print("Searching for document after delete")
pprint.pprint(accounts_collection.find_one(document_to_delete))
print("Documents deleted: ", str(result.deleted_count))

client.close()