from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017")

db = client["ctip"]

enriched_collection = db["enriched_logs"]

correlation_collection = db["correlations"]