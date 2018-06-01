#! /usr/bin/python3
# coding=utf-8
'''
Created on 2018年5月24日

@author: qcymkxyc
'''

import queue
from lib.utility.mongo_helper import MongoDBHelper

class MongoSaver(object):
    """
        通过MongoDB保存
    """
    mongodb_helper = MongoDBHelper()
    
    @staticmethod
    def save_data(collection_name,data):
        collection_name = collection_name[collection_name.find("/") + 1 : collection_name.find(".")]
        if isinstance(data, queue.Queue):
            MongoSaver.save_queue(collection_name, data)
        elif isinstance(data, list):
            MongoSaver.save_list(collection_name, data)


    @staticmethod
    def save_list(collection_name,data):
        """list类型保存"""
        for sub_data in data:
            MongoSaver.mongodb_helper.insert(collection_name,sub_data)
                 
    @staticmethod                    
    def save_queue(filename,data):
        """队列数据存储"""
        pass
