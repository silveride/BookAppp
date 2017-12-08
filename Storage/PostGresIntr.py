# -*- coding: utf-8 -*-

import psycopg2 as pg

# Create One interface for a DB
class PostGresDBInterface:
    def __init__(self, dbname='dvdrental', user='postgres', password ='mathew'):
        print("Initializing the postgres interface")
        self.databaseName = dbname
        self.userName = user
        self.password = password
        self.initScriptName = ""
    
    def setInitScript(self, initScripName):
        self.initScriptName = initScriptName
        
    def startInterface(self):
        self.connection = pg.connect(database=self.databaseName, user= self.userName, password = self.password)
        self.cursor = self.connection.cursor()
        if (self.initScriptName !="" ):
            initialiseDB(initScriptName) # init script contains sql statements seperated by ;
        
    def stopInterface(self):
        self.connection.close()
        
    def executeStatement(self,statement):
        self.cursor.execute(statement)
        
    def fetchResult(self, numberOfResult=-1):
        if (numberOfResult == -1):
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchmany(numberOfResult)
            
    def initialiseDB(self,initScriptName):
        statements = getStatementsFromFile(initScriptName)
        # execute one after the other
        for statement in statments:
            executeStatement(statement)
            
    def getStatementsFromFile(self,fileName,delimiter=';'):
        fd = open(initScriptName,'r')
        # read each sql statement endind in ;
        buffer = fd.read()
        statements = buffer.split(delimiter)
        return statements
        
if __name__ == "__main__":
    print ("Debug on: PostGresSQL")
    pgIntr = PostGresDBInterface()
    pgIntr.startInterface()
    # pgIntr.setInitScript()
    statement = 'SELECT * FROM CUSTOMER'
    pgIntr.executeStatement(statement)
    results = pgIntr.fetchResult()
    
    # Result is a list of tuples
    for row in results:
        for element in row:
            print(element,end=',')
        print('\n')
    
    print("Size:" + str(len(results)))
    