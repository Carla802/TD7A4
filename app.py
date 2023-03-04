from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient("mymongo")
db = client["td5"]
collection = db["Collection_TD5"]

tab = {"name": "Carla", "age": 20}

collection.insert_one(tab)

file_path = os.path.abspath('data.txt')

@app.route('/td6')
def index():
    with open(file_path, 'r') as file:
        content = file.read()
    return content

@app.route("/")
def hello():
	data= collection.find_one()
	return str(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
