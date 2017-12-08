# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:24:43 2017

@author: mmathew
"""


from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table
import time

class DynamoIntr:
    def __init__(self):
        print ("Initialising dynamo")
        self.access_key = "foo"
        self.access_sid = "bar"
        self.hostname = "localhost"
        self.port = 8000
        self.inited = 0
        
    def open(self):
        self.conn = DynamoDBConnection(aws_access_key_id=self.access_key, aws_secret_access_key=self.access_sid, host=self.hostname, port = self.port, is_secure=False)
        self.status = 1


    def initTable(self):
        if self.status == 1 and self.inited == 0:
            self.table = Table.create('KeySet', schema=[HashKey('id')], connection = self.conn)
            self.table.describe()
            self.inited = 1
            
        
    def set(self,key,value):
        if self.status == 1:
            self.table.put_item(data = {'id':key, 'dateAdded':time.time(), 'value':value})
            
        else:
            print("Redis accessed witout initialisation")

    # if the key is not present None is returned.            
    def get (self,key):
        if self.status == 1:
            return self.table.get_item(id = key)
            
    def printConfig(self):
        print("Configuration of Dynamo")
        print("hostname:"+self.hostname)
        print("port:"+ str(self.port))
        print("status:"+str(self.status))
                

if __name__ == "__main__":
    print ("Debug on:")
    red = DynamoIntr()
    red.open()
    red.initTable();
    red.set('foo','bar')
    red.printConfig()
    print((red.get('Alex')))
    
    