import os
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MoONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MoONGODB_URI)

db=client.bank

accounts_collection = db.accounts

new_accounts=[{
    "account_holder": "Ajay Bhai",
    "account_id": "129456989",
    "account_type": "checking",
    "balance": 179797.50,
},
{
    "account_holder": "Harsh Bhai",
    "account_id": "12356789",
    "account_type": "savings",
    "balance": 89000.50,
},
]

#Insert Many method
result=accounts_collection.insert_many(new_accounts)

document_ids=result.inserted_ids
print("# of documents inserted: ", str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()