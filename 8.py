# Importaciones de librerias
import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId

# Conexión a couchdb
URL = "http://admin:admin@127.0.0.1:5984"
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print("CouchDB connection: Success")
    if response.status_code == 401:
        print("CouchDB connection: failed", response.json())
except requests.ConnectionError as e:
    raise e
server = couchdb.Server(URL)

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
db = server["olimpiccities"]
# Conexión con mongodb atlas
client = MongoClient("mongodb+srv://user1:user1@menu.xjcpf.mongodb.net/test")
try:
    client.admin.command("ismaster")
    print("MongoDB connection: Success")
except ConnectionFailure as cf:
    print("MongoDB connection: Failed", cf)

dbs = client.get_database("correccionExamen")

db_one = dbs.Twitter
# Lectura de la base en couch y escritura en mongodb atlas
for id in db:
    if(db_one.find_one({"_id": db[id].id})):
        print("This id of the document already exist")
    else:
        db_one.insert_one(db[id])
