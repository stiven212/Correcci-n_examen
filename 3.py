# Importación de librerias y conexión con mongodb
from bson.raw_bson import RawBSONDocument
import json
import bson
import pandas as pd
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
myClient = MongoClient('mongodb://localhost:27017/')
try:
    myClient.admin.command('ismaster')
    print('MongoDB connection: Succes')
except ConnectionFailure as cf:
    print('MongoDB connection: Succes', cf)


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def find_1st(string, substring):
    return string.find(substring, string.find(substring))


response = requests.get('https://olympics.com/tokyo-2020/es/')
soup = BeautifulSoup(response.content, "lxml")

Titles = []

# Selección del elemento html común
post_titles = soup.find_all("span", class_="tk-card__titlelink")

# for para limpiar
for element in post_titles:

    element = str(element)
    limpio = str(element[find_1st(element, '>')+1:find_2nd(element, '<')])

    Titles.append(limpio.strip())


# Creación de una base de datos y colección con lo recopilado
archivo = pd.DataFrame(Titles, index=Titles)
archivo.to_json('datos.json')

db = myClient["JuegosO"]
Collection = db["noticias"]

with open('datos.json') as file:
    file_data = json.load(file)


if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)
