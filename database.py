from pymongo import MongoClient
import streamlit as st
#from config import MONGO_URI, DATABASE_NAME

def get_database():
    client = MongoClient(st.secrets['MONGO_URI'])
    return client[st.secrets['DATABASE_NAME']]

MONGO_URI = "mongodb+srv://sadityain:dTnronjU9pdDsp92@cluster0.6f5iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "project_management"