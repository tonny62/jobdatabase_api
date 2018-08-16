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

def reformat(result):
    newresult = []
    # Reformat data into label and value, result is list of dictionary of a row
    for row in result:
        newrow = {}
        for col in row:
            if ("label" in col):
                if (newrow.get('label') == None):
                # label item doesn't exists
                    newrow.update({'label' :
                                       { col.split("_")[1] : str(row.get(col)) }
                                   })
                else:
                    newrow['label'].update({col.split("_")[1] : str(row.get(col))})
            elif(col == 'value'):
                # convert decimal to int
                if(row[col] != None):
                    newrow.update({'value': int(row[col])})
            else:
                newrow.update({col : row[col]})
        newresult.append(newrow)
    return newresult

def getData(monthfrom, monthto):
    dbconn = db.dbDriver()
    queries = getqueries(monthfrom, monthto)
    results = {}
    for query in queries:
        result = dbconn.read(query[1])
        result = reformat(result) # result is list of row dictionaries
        results.update({query[0] : result})
    return results
