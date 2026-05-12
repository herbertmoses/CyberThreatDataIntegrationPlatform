from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017")

db = client["ctip"]

normalized_collection = db["normalized_logs"]

enriched_collection = db["enriched_logs"]