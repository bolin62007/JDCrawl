#!/usr/bin/python3
#coding=utf8
'''
Created on 2018年5月23日

@author: qcymkxyc
'''

import queue
import os
import conf

class TxtSaver(object):


    @staticmethod
    def save_data(filename,data):
        if not os.path.exists(conf.save_folder):
            os.mkdir(conf.save_folder)
        if isinstance(data, queue.Queue):
            TxtSaver.save_queue(filename, data)
        elif isinstance(data, list):
            TxtSaver.save_list(filename, data)


    @staticmethod
    def save_list(filename,data):
        """list类型保存"""
        with open(filename,"w") as f:
            headers = None
            for sub_data in data:
                if not headers:
                    headers = sub_data.keys()
                    f.write(" ".join(headers))
                sub_data_list = [str(x) for x in sub_data.values()]
                f.write(" ".join(sub_data_list))
                 
        
        
    @staticmethod                    
    def save_queue(filename,data):
        """队列数据存储"""
        pass
    