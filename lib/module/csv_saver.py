#! /usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月24日

@author: qcymkxyc
'''

import csv
import queue

class CSVSaver(object):
    """CSV存储器"""
    def __init__(self):
        pass
    
    @staticmethod
    def save_data(filename,data):
        with open(filename,"w") as f:
            if isinstance(data, queue.Queue):
                while not data.isEmpty():
                    data.get()

    @staticmethod                    
    def save_queue(filename,data):
        """队列数据存储"""
        with open(filename,"w") as f:
            fieldnames = None
            while not data.empty():
                sub_data = data.get()
                if not fieldnames:
                    fieldnames = sub_data.keys()
                    writer = csv.DictWriter(f,fieldnames = fieldnames)
                writer.writeheader()
                writer.writerow(sub_data)
                
                    
                
            