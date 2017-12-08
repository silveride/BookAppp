# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:30:48 2017

@author: mmathew
"""

import redis

class redisIntr:
    def __init__(self):
        self.name = "cache"
        self.hostname = "localhost"
        self.port = 6379
        self.db=0
        self.status = 0
        
    def open(self):
        self.red = redis.StrictRedis(host=self.hostname, port=self.port,db=self.db)
        self.status = 1


    def set(self,key,value):
        if self.status == 1:
            self.red.set(key,value)
        else:
            print("Redis accessed witout initialisation")

    # if the key is not present None is returned.            
    def get (self,key):
        if self.status == 1:
            return self.red.get(key)
            
    def printConfig(self):
        print("Configuration of Redis")
        print("hostname:"+self.hostname)
        print("port:"+ str(self.port))
        print("status:"+str(self.status))
        print("maxmemory:"+self.red.config_get('maxmemory')['maxmemory'])
        print("maxmemory:"+self.red.config_get('maxmemory-policy')['maxmemory-policy'])
                

if __name__ == "__main__":
    print ("Debug on:")
    red = redisIntr()
    red.open()
    red.set('foo','bar')
    red.printConfig()
    print(red.get('foo'))
    
    