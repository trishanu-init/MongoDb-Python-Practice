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

usd_to_inr = 82.0
#Convert USD to INR

select_accounts = {"$match": {"acconunt_type": "checking","balance": {"$gt": 100}}}
#highest to lowest balance
organize_by_original_balance = {"$sort": {"balance": -1}}

return_specific_fields = {
    "$project":{
        "account_type": 1,
        "balance": 1,
        "inr_balance": {"$multiply": ["$balance", usd_to_inr]},
        "_id": 0,
    }
}

pipeline=[
    select_accounts,
    organize_by_original_balance,
    return_specific_fields,
]

result=accounts_collection.aggregate(pipeline)

print("Account type, original balance and balance in INR of all checkings accounts with balance greater than 1000:","\n")

for i in result:
    pprint.pprint(i)


client.close()