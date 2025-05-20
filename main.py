from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
from enum import Enum
import pymongo

# db=client.get_database("fastapi") 
# item_transaction=db.get_collection("item_transaction")

application = FastAPI() 

class methodType(str, Enum):
    credit = "credit"
    debit = "debit"
    cash = "cash"

class Item(BaseModel):
    name: str
    price: Optional[float] = None
    method: methodType

uri="mongodb+srv://admin:<admin123>@cluster0.grl9mt1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=pymongo.MongoClient(uri)
    
item_transaction = []

# Quarry Parameters
@application.get("/transaction")
async def get_transaction(tipe:Optional[methodType] = None,):
    if tipe is None:
        return item_transaction
    filtered_items = [item for item in item_transaction if item.method == tipe]
    return filtered_items
    

# path parameters
@application.get("/transaction/{name}/{amount}")
async def get_transaction(name: str, amount: float):
    return f"Transaction for {name} of amount {amount} processed successfully."

@application.post("/transaction/")
async def post_transaction(input_transaction: Item):
    # item_transaction.insert_one(input_transaction)
    return item_transaction
