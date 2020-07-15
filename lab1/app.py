from flask import Flask
from bson.json_util import dumps
import json

app = Flask(__name__)

@app.route("/add", methods = ['POST'])
def add_contact() :
    data = json.loads(request.data)
    desc = data['desc']
    if desc :
        # insert in database
        return dumps({ 'message' : 'SUCCESS' })
        
@app.route("/get", methods = ['GET'])
def get_all_contact() :
    # get from database
    return dumps({ '0':{'desc': 'buy grocery'},'1' : {'desc': 'pay bills'} })

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    
