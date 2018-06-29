import json
import mysql.connector as mysqlconn
import pandas as pd
from src import dbdriver as db

def getData(monthfrom, monthto):
    query = '''SELECT job.jobid, job.ostarnetid, job.postdate, job.jobtitle, jc.companyname, jc.industrynameEN, jc.provinceNameEN
    FROM job
    LEFT JOIN (
        SELECT companyid, companyname, provinceNameEN, industryNameEN, jpno FROM company
        LEFT JOIN province ON company.provinceid = province.provinceid
        LEFT JOIN industry ON company.industryid = industry.industryid
    ) as jc ON job.companyid = jc.companyid

    LEFT JOIN (
        SELECT jobid, major.majorid, majorNameEN FROM job_has_major
                LEFT JOIN major ON major.majorid = job_has_major.majorid) AS jm
        ON job.jobid = jm.jobid
'''
    dbconn = db.dbDriver()
    result = dbconn.read(query)

    ## query the database then put into the result dataframe
    #result = pd.DataFrame({"jobtitle": ["job1","job2","job3"],
        #"jobid": [4,5,6]})



    response = result.to_dict(orient='records')

    return response
