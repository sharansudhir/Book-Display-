from flask import Flask
from flask import jsonify, request, render_template
from flask_cors import CORS, cross_origin
import json
import os.path
from os import path

app = Flask(__name__)

cors = CORS(app)


@app.route('/notes', methods=['POST'])
def notes():
    notes = request.form
    for x in notes.keys():
        data = x
    data_dict = json.loads(data)
    keyword = data_dict['keyword'].split(",")[0]
    note = data_dict['keyword'].split(",")[1]

    entry = {keyword: note}

    if (path.exists("notes.json")):
        flag=0
        with open("notes.json", mode='r+', encoding='utf-8') as f:
            s = f.read()
            x = json.loads(s)
            for a in x:
                f = a.keys()
                z = list(f)[0]
                if keyword in z:
                    a[keyword] = a[keyword] + " , " + note
                    flag=1
                    break

        if(flag==1):
            with open("notes.json", mode='w+', encoding='utf-8') as f:
                f.write(json.dumps(x,indent=2))
        else:
            x.append(entry)
            with open("notes.json", mode='w+', encoding='utf-8') as f:
                f.write(json.dumps(x,indent=2))

    else:
        with open("notes.json", mode='w', encoding='utf-8') as f:
            f.write(json.dumps([entry], indent=2))

    return jsonify("Note Save Request Successful")

@app.route('/notes_search', methods=['POST'])
def notes_search():
    notes = request.form
    for x in notes.keys():
        data = x
    keyword= json.loads(data)
    flag=0
    with open("notes.json", mode='r+', encoding='utf-8') as f:
        s = f.read()
        x = json.loads(s)
        for a in x:
            f = a.keys()
            z = list(f)[0]
            if keyword in z:
                flag=1
                break

        if(flag==1):
            print("Found")
            s=a
        else:
            print("Not found")
            s=''
    return jsonify(s)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5300,debug=True)
