from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

def get_database():
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]