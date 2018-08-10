from flask import Flask, request, jsonify
import json
from src import queryFactory, mylogger

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return "<h1>JOB DATABASE API SERVER</h1>"

@app.route('/api/testpost', methods=['POST'])
def testpost():
    print(request.form)
    return jsonify(request.form)

@app.route('/api/getdata', methods=['POST'])
def getdata():
    try:
        datain = request.form
        ## extract parameters
        monthfrom = datain['startDate']
        monthto = datain['endDate']
        datenow = datain['currentTime']

        ## receive json response from queryfactory type dictionary
        queryData = queryFactory.getData(monthfrom, monthto)

        ## create correct response JSON
        response = queryData

        if(not response):
            mylogger.writelog("ERROR LINE 30 : "+str(request.form))
            return "ERROR 404"
        else:
            mylogger.writelog("INCOMING REQUEST : " + str(request.form))
            return jsonify({"job": response})
    except:
        mylogger.writelog("ERROR LINE 37 INVALID REQUEST : " + 
                str(request.form))
        return "Expecting fields name = startDate, endDate, currentTime"
