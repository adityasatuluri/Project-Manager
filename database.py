from pymongo import MongoClient
import streamlit as st
#from config import MONGO_URI, DATABASE_NAME

def get_database():
    client = MongoClient(st.secrets[MONGO_URI])
    return client[st.secrets[DATABASE_NAME]]