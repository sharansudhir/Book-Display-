from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify,request,render_template
from flask_cors import CORS, cross_origin
import json
import os
import datetime

times = datetime.datetime.now()

app = Flask(__name__)

cors = CORS(app)


@app.route('/logs',methods = ['POST'])
def logs():
    search = request.form

    for x in search.keys():
        data = x
    data_dict = json.loads(data)
    search_term = data_dict['search_term']

    dcit ={}
    if(not os.path.exists("log.txt")):
        count=1
        with open("log.txt","w+") as f:
            s = str(times)+","+str(search_term) + "," + str(count)+"\n"
            f.writelines(s)
    else:
        with open("log.txt","r+") as f:
                for i  in f.readlines():
                    dcit[i.split(',')[1]] = int(i.split(',')[2].split()[0])

        if(search_term in dcit.keys()):
            dcit[search_term] = dcit[search_term]+1
            with open("log.txt","w+") as f:
                for i in dcit:
                    s = str(times)+","+str(i)+","+str(dcit[i])+"\n"
                    f.writelines(s)
        else:
            count=1
            with open("log.txt", "a+") as f:
                s = str(times)+","+str(search_term) + "," + str(count) + "\n"
                f.writelines(s)

    x= "LOG FILE SAVED"
    return jsonify(x)


if(__name__ == "__main__"):
    app.run(host='0.0.0.0',debug =True,port=5100)