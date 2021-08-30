# Importación librerias
import requests
from pymongo import MongoClient
import couchdb

# Conexión con couchdb
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

# Conexión con Mongodb
client = MongoClient("mongodb://localhost:27017")
try:
    client.admin.command("ismaster")
    print("MongoDB connection: Success")
except ConnectionFailure as cf:
    print("MongoDB connection: Failed", cf)

dbs = client.get_database("FromCouch")

db_one = dbs.C2

# Iteración dentro de la base de datos

for id in db:
    if(db_one.find_one({"_id": db[id].id})):
        print("This id of the document already exist")
    else:
        db_one.insert_one(db[id])
