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

#Update Many method
select_accounts={"accont_type": "checking"}

set_field={"$set": {"minimum_balance": 100}}

result=accounts_collection.update_many(select_accounts, set_field)
print("Documents updated: ", str(result.modified_count))
print("Documents matched: ", str(result.matched_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()