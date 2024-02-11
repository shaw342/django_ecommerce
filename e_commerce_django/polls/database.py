from django.db import models
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os


class Models:
    def connectionDatabase():
        uri = os.getenv("MONGO_URL")
        client = MongoClient(uri, server_api=ServerApi('1'))
        db =  client["e_commerce_django"]
        return db
    
    def addCustomers(data):
        db = Models.connectionDatabase()
        Customers = db["Customers"]
        Customers.insert_one(data)