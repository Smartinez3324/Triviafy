from game.user import User 
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD", "")
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME", "")

class DataBase:
    def __init__(self):
        uri = "mongodb+srv://" + MONGO_DB_USERNAME + ":"+ MONGO_DB_PASSWORD +"@triviafy.hq1x6.mongodb.net/?retryWrites=true&w=majority&appName=Triviafy"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        self.client = client
