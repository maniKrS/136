from flask import Flask
from bata import data2
from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route("/")

def myFunction ():
    return jsonify({
        "data":data2,
         "message":'success',

    }),200
@app.route("/planets")
def myfunction2():
    name=request.args.get("name")
    planet_data = next(item for item in data2 if item["name"]==name)
    return jsonify({
        "data":planet_data,
        "message":'success'
    }),200

if __name__=="__main__":
    app.run()