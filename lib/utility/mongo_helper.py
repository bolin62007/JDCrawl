#! /usr/bin/python3 
#coding=utf-8

'''
Created on 2018年5月23日

@author: qcymkxyc
'''

import pymongo
import conf

class MongoDBHelper(object):
    def __init__(self):
        #获取连接参数以及数据库参数
        self.__conn_dict = conf.mongo_conn_dict
        self.__db_name = conf.mongo_db_name
        
        self.__conn = MongoDBHelper.get_conn(self.__conn_dict);
        
    @staticmethod
    def get_conn(conn_dict):
        """返回连接
            @param conn_dict:连接参数的字典形式
            @return: 连接对象 
        """
        return pymongo.MongoClient(**conn_dict)
        
        
    def insert(self,collection_name,data):
        conn = self.__conn
        db = conn[self.__db_name]
        collection = db[collection_name]
        collection.insert(data)
        
    
    def find(self):
        pass
        
    
    def close(self):
        self.__conn.close()
        
        