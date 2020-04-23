from flask import Flask
from flask import jsonify, request, render_template
from flask_cors import CORS, cross_origin
import json
import os

app = Flask(__name__)

cors = CORS(app)


@app.route('/catalogue', methods=['POST'])
def catalogue():
    data = request.form
    for x in data.keys():
        data_extract = x
    data_dict = json.loads(data_extract)
    print(data_dict)
    if(os.path.exists("catalogue.json")):

        with open("catalogue.json", mode='r+', encoding='utf-8') as f:
            s = f.read()
            x = json.loads(s)
            for i in x:
                data_dict.append(i)
        with open("catalogue.json", mode='w+', encoding='utf-8') as f:
            f.write(json.dumps(data_dict, indent=2))
    else:
        with open("catalogue.json", mode='w+', encoding='utf-8') as f:
            f.write(json.dumps(data_dict, indent=2))
    return jsonify("Catalogue Request Successful")


if (__name__ == "__main__"):
    app.run(host='0.0.0.0',debug=True, port=5200)
