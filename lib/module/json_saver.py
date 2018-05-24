#!/usr/bin/python3
#coding=utf8
'''
Created on 2018年5月23日

@author: qcymkxyc
'''
import json

def save_json(filename,data):
    """将数据保存为json格式"""
    with open(filename,"w",encoding = "utf-8") as f:
        for i in data:
            json.dump(i,f,ensure_ascii = False)
    