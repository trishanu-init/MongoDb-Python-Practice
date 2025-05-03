import os
import pprint
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MoONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MoONGODB_URI)

def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):
    account_collection= session.client.bank.accounts
    transfers_collection= session.client.bank.transfers

    transfer= {
          "transfer_id": transfer_id,
          "to_account": account_id_receiver,
          "from_account": account_id_sender,
          "amount": {"$numberDecimal":transfer_amount},
    }

    account_collection.update_one(
        {"account_id": account_id_sender},
        { 
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
    session=session,
    )

    transfers_collection.insert_one(transfer, session=session)
    print("Transaction complete")
    return

def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="992356789",
        account_id_sender="111956989",
        transfer_amount=100,
    )

with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()