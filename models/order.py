from pymongo import MongoClient
from bson.objectid import ObjectId
from config import config

# Connect to the MongoDB database
client = MongoClient(config.MONGODB_URI)
db = client['ecommerce_db']
orders_collection = db['orders']

def create_order(user_id, products, total_price):
    """Create a new order"""
    order = {
        "user_id": user_id,
        "products": products,  # List of products (including ID and quantity)
        "total_price": total_price,
        "status": "pending"  # Initial order status
    }
    return orders_collection.insert_one(order).inserted_id

def get_order(order_id):
    """Retrieve an order by its ID"""
    return orders_collection.find_one({"_id": ObjectId(order_id)})

def update_order_status(order_id, status):
    """Update the status of an order"""
    return orders_collection.update_one({"_id": ObjectId(order_id)}, {"$set": {"status": status}})

def delete_order(order_id):
    """Delete an order by its ID"""
    return orders_collection.delete_one({"_id": ObjectId(order_id)})
