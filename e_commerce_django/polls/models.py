from django.db import models
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
uri = os.getenv("MONGO_URL")
client = MongoClient(uri, server_api=ServerApi('1'))
db =  client["e_commerce_django"]
person_collection = db["Customers"]

class Models:
    def connection():
        uri = os.getenv("MONGO_URL")
        client = MongoClient(uri, server_api=ServerApi('1'))
        db =  client["e_commerce_django"]
        return db
    
    def addCustomers(data):
        db = Models.connection()
        Customers = db["Customers"]
        Customers.insert_one(data)
    