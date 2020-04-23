from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify, request, render_template
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_DBNAME'] = "my_db"
app.config["MONGO_URI"] = "mongodb://localhost:27017/my_db"
mongo = PyMongo(app)


@app.route('/search', methods=['POST'])
def search():
    result = []
    search = request.form
    for x in search.keys():
        data = x
    data_dict = json.loads(data)
    search_term = data_dict['search_term']
    search = mongo.db.my_collection
    search_query = {"$text": {"$search": search_term}}
    cursor = search.find(search_query)
    for i in cursor:
        result.append({"book": i["book"], "author": i["author"]})

    x = jsonify(result)
    x.headers['Access-Control-Allow-Origin'] = '*'
    return x


if (__name__ == "__main__"):
    app.run(host='0.0.0.0',debug=True,port=5000)
