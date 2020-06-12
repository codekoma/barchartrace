from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from pymongo import MongoClient
import datetime
import json
from bson import ObjectId

app = Flask(__name__)
api = Api(app)
CORS(app)

# date = datetime.date.today()
connection = MongoClient('localhost', 27017)
db = connection['MAX_OI']
collec = db['oi_collec']



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class getdata(Resource):
    support_cors = True
    cors_origin = '*'
    cors_headers = 'origin,content-type,x-request-with'

    def get(self):
        data = []
        raw = collec.find()
        for d in raw:
            d["_id"] = JSONEncoder().encode(d["_id"])
            data.append(d)
        return data
        

api.add_resource(getdata, "/getdata")
app.run(debug=True)
