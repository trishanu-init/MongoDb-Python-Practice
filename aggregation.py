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

select_by_balance = {
    "$match": {
        "balance": {
            "$lt": 100000
        }
    }
}

seperate_by_account_calculate_avg_balance = {
    "$group": {
        "_id": "$account_type",
        "avg_balance": {
            "$avg": "$balance"
        }
    }
}

pipeline=[
    select_by_balance,
    seperate_by_account_calculate_avg_balance,
]

result=accounts_collection.aggregate(pipeline)

print()
print("Average balance of accounts with balance less than 100000:","\n")

for i in result:
    pprint.pprint(i)

client.close()