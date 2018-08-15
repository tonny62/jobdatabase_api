from flask import Flask, request, jsonify, Response
import json
from src import queryFactory, mylogger
import simplejson
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def home():
    return "<h1>JOB DATABASE API SERVER</h1>"


@app.route('/api/testpost', methods=['POST'])
def testpost():
    mydict = request.get_json()
    print(mydict)
    return mydict


@app.route('/api/getdata', methods=['POST'])
def getdata():
#    datain = request.form
#    ## extract parameters
#    monthfrom = datain['startDate']
#    monthto = datain['endDate']
#    datenow = datain['currentTime']

    datain = request.get_json()
    if(datain != None):
        try:
            print(datain)
            monthfrom = datain['startDate']
            monthto = datain['endDate']
            datenow = datain['currentTime']
        else:
            monthfrom = ""
            monthto = ""
            datenow = ""
    else:
        print(datain)
        monthfrom = ""
        monthto = ""
        datenow = ""

    ## create dicts of query result
    response_data = queryFactory.getData(monthfrom, monthto)
    response_data = simplejson.dumps(response_data)  # simplejson could encode Decimal

    ## create correct response JSON
    response = Response(response_data, mimetype='application/json')

    return response


    # if(not response):
    #     mylogger.writelog("ERROR LINE 30 : "+str(request.form))
    #     return "ERROR 404"
    # else:
    #     mylogger.writelog("INCOMING REQUEST : " + str(request.form))
    #     return str({"job": response})
    #
    # mylogger.writelog("ERROR LINE 37 INVALID REQUEST : " +
    #         str(request.form))
    # return "Expecting fields name = startDate, endDate, currentTime"
