from pymongo import MongoClient

client = pymongo.MongoClient(host="mongodb://localhost:8000")
result = client.admin.command("isMaster") 
db = client['db-name']
