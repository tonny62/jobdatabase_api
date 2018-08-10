import json
import mysql.connector as mysqlconn
import pandas as pd
from src import dbdriver as db

def getData(monthfrom, monthto):
    query = '''SELECT job.jobid as JOB_ID,
    job.ostarnetid as ONET_SOC,
    job.postdate as date_posted,
    job.jobtitle as job_title,
    jc.companyname as company,
    jc.industrynameEN as industry, 
    jc.provinceNameEN as province
    FROM job
    LEFT JOIN (
        SELECT companyid, companyname,
        provinceNameEN, industryNameEN,
        jpno 
        FROM company
        LEFT JOIN province 
            ON company.provinceid = province.provinceid
        LEFT JOIN industry 
        ON company.industryid = industry.industryid
    ) as jc 
    ON job.companyid = jc.companyid
    LEFT JOIN (
        SELECT jobid, 
        major.majorid, 
        majorNameEN 
        FROM job_has_major
        LEFT JOIN major 
            ON major.majorid = job_has_major.majorid) AS jm
        ON job.jobid = jm.jobid
'''
    dbconn = db.dbDriver()
    result = dbconn.read(query)

    ## query the database then put into the result dataframe
    response = result.to_dict(orient='records')

    return response
