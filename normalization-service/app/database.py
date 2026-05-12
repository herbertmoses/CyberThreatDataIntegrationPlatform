from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017")

db = client["ctip"]

raw_collection = db["raw_logs"]
normalized_collection = db["normalized_logs"]