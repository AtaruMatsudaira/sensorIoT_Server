from flask import Flask,request,jsonify
import time

app = Flask(__name__)

dataDic = dict()

@app.route('/')
def neko():
    return "<h1>にゃーん</h1>"

@app.route("/post",methods=["POST"])
def post():
    vec_len = request.json["accX"]+request.json["accY"]+request.json["accZ"]
    dataDic[time.time()] = vec_len
    return "success"

@app.route("/get")
def get():
    return jsonify(dataDic)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",threaded = True)