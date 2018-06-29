from flask import Flask, request, jsonify
import json
from src import queryFactory

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return "<h1>API SERVER najaaaa</h1>"

@app.route('/api/getdata', methods=['POST'])
def getdata():
    datain = request.form
    ## extract parameters
    monthfrom = datain['startDate']
    monthto = datain['endDate']
    datenow = datain['currentTime']

    ## receive json response from queryfactory
    response = queryFactory.getData(monthfrom, monthto)

    if(not response):
        return "ERROR404"
    else:
        return jsonify({"job": response})
