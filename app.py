from flask import Flask,request,jsonify
import time
import json
import asyncio
import math

app = Flask(__name__)

data_dic = dict()

def save_data():
    with open("dump.json","w") as f:
        f.write(json.dumps(data_dic))

def load_data():
    global data_dic
    with open("dump.json","r") as f:
        data_dic = dict(json.load(f))
        
@app.route('/')
def neko():
    return "<h1>にゃーん</h1>"

@app.route("/post",methods=["POST"])
def post():
    vec_len = math.sqrt(request.json["accX"]**2+request.json["accY"]**2+request.json["accZ"]**2)
    data_dic[str(time.time())] = vec_len
    return "success"

@app.route("/get")
def get():
    return data_dic

async def save_task():
    while True:
        await asyncio.sleep(30)
        save_data()

if __name__ == "__main__":
    load_data()
    app.run()
    save_task()
    