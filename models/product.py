from pymongo import MongoClient
from bson.objectid import ObjectId
from config import config

# Connect to the MongoDB database
client = MongoClient(config.MONGODB_URI)
db = client['ecommerce_db']
products_collection = db['products']

def add_product(name, description, price, category_id):
    """Add a new product to the database"""
    product = {
        "name": name,
        "description": description,
        "price": price,
        "category_id": category_id
    }
    return products_collection.insert_one(product).inserted_id

def get_product(product_id):
    """Retrieve a product by its ID"""
    return products_collection.find_one({"_id": ObjectId(product_id)})

def update_product(product_id, update_data):
    """Update the information of a product"""
    return products_collection.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})

def delete_product(product_id):
    """Delete a product by its ID"""
    return products_collection.delete_one({"_id": ObjectId(product_id)})
