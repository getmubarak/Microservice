from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json

app = Flask(__name__)

mongodb_host = os.environ.get('MONGO_HOST', 'localhost')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))
client = MongoClient(mongodb_host, mongodb_port)   
db = client.TodoDB

@app.route("/add", methods = ['POST'])
def add_contact() :
    data = json.loads(request.data)
    desc = data['desc']
    if desc :
        status = db.Todo.insert_one({"desc" : desc})
        return dumps({ 'message' : 'SUCCESS' })
        
@app.route("/get", methods = ['GET'])
def get_all_contact() :
    todos = db.Todo.find()
    return dumps(todos)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
