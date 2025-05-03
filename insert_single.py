import os
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MoONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MoONGODB_URI)

db=client.bank

accounts_collection = db.accounts

new_account={
    "account_holder": "Linus Bhai",
    "account_id": "123456989",
    "account_type": "checking",
    "balance": 1000.50,
    "last_updared": datetime.datetime.utcnow()
}

#Insert one method
result=accounts_collection.insert_one(new_account)

document_id=result.inserted_id
print(f"New account created with _id: {document_id}")

client.close()