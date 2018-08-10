from src import dbdriver as db
import os

def getqueries(monthfrom, monthto):
    path = "./queries/"
    files = os.listdir(path)
    queries = []
    for item in files:
        if(item == ".git"):
            continue
        with open(path+item, 'r') as fin:
            lines = fin.readlines()
            query = " ".join([line.strip() for line in lines])

            # return queries as (queryname, querytext)
            print(item.split(".")[0], "is querying")
            queries.append((item.split('.')[0], query))

    return queries

def getData(monthfrom, monthto):
    dbconn = db.dbDriver()
    queries = getqueries(monthfrom, monthto)
    results = {}
    for query in queries:
        result = dbconn.read(query[1])
        results.update({query[0] : result})

    ## query the database then put into the result dataframe
    # response = result.to_dict(orient='records')

    return results
