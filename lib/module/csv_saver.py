#! /usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月24日

@author: qcymkxyc
'''

import csv
import queue
import conf
import os

class CSVSaver(object):
    """CSV存储器"""
    def __init__(self):
        pass
    
    @staticmethod
    def save_data(filename,data):
                #创建保存文件夹
        if not os.path.exists(conf.save_folder):
            os.mkdir(conf.save_folder)
        
        if isinstance(data, queue.Queue):
            CSVSaver.save_queue(filename, data)
        elif isinstance(data, list):
            CSVSaver.save_list(filename, data)


    @staticmethod
    def save_list(filename,data):
        """list类型保存"""
        with open(filename,"w") as f:
            fieldnames = None;
            for sub_data in data:
                if not fieldnames:
                    fieldnames = sub_data.keys()
                    writer = csv.DictWriter(f,fieldnames = fieldnames)
                    writer.writeheader()
                try:
                    writer.writerow(sub_data)
                except ValueError:
                    continue;
                 
        
        
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
                
                    
                
            