import pandas as pd
import mysql.connector
import configparser as cp


class dbDriver:
    def __init__(self):
        parser = cp.ConfigParser()
        parser.read("src/config.ini")
        self.serverip = parser['DATABASE']['serverip']
        self.userid = parser['DATABASE']['id']
        self.password = parser['DATABASE']['password']
        self.database = parser['DATABASE']['database']

    def getConnection(self):
        connection = mysql.connector.connect(user=self.userid,
                password=self.password, host=self.serverip,
                database=self.database)
        return connection

    def read(self, query, arguments=None):
        try:
            if(arguments != None):
                if (type(arguments) != tuple):
                    raise TypeError("arguments is not of type tuple")
                    return None
                else:
                    cnx = self.getConnection()
                    cursor = cnx.cursor()
                    cursor.execute(query, arguments)
            else:
                cnx = self.getConnection()
                cursor = cnx.cursor()
                cursor.execute(query)
            ## craft dataframe
            header = [item if type(item) == str else item.decode() for item in cursor.column_names]
            print(header)
            outData = pd.DataFrame(data=cursor.fetchall(), columns=header)


        except:
            ## catch some error
            outData = None
        finally:
            ## always close connection
            cnx.close()

        ## return pandas DataFrame
        return outData.to_dict(orient='records')

    def update(self, query, arguments=None):
        try:
            result = True
            if(arguments != None):
                if (type(arguments) != tuple):
                    raise TypeError("arguments is not of type tuple")
                cnx = self.getConnection()
                cursor = cnx.cursor()
                cursor.execute(query, arguments)
            else:
                cnx = self.getConnection()
                cursor = cnx.cursor()
                cursor.execute(query)
            cnx.commit()
        except:
            result = None
        finally:
            cnx.close()
        return result

