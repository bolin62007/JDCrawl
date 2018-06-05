#!/usr/bin/python3
#coding=utf8
'''
Created on 2018年5月17日

@author: leonlee
'''
from lib.module import json_saver
from lib.module import csv_saver
from lib.module.mongo_saver import MongoSaver

###############################################################
#    爬虫配置
##############################################################
base_url = "https://sclub.jd.com/comment/productPageComments.action?"
comment_crawl_params = {
    "callback" : "fetchJSON_comment98vv283",
    "productId" : 27555188739,
    "score" : 0,
    "sortType" : 5,
    "page" : 0,
    "fold" : 1,
    "pageSize" : 10,
    "isShadowSku" : 0
}
#爬取评论的正则表达式
crawl_comment_rule = "{\"id\":\d+,\"topped\".+?\"afterDays\":\d+?}" 

#商品列表网址
items_url = "https://list.jd.com/list.html?cat=1713,3287,3804&go=0"

###################################################################
#    数据库配置
#####################################################################
mongo_conn_dict = {
    "host" : "139.199.128.90",
    "port" : 27017
}
mongo_db_name = "JDCrawl"

#######################################################################
#    线程池配置
#######################################################################
#最大线程数
max_threads = 10
#爬取评论的页数
max_page = None

########################################################################
#    其他
########################################################################
#保存方式
save_ways = {
            "csv" : csv_saver.CSVSaver.save_data,
            "mongodb": MongoSaver.save_data,
            "txt" : json_saver.TxtSaver.save_data
            }
#默认保存评论的文件夹
save_folder = "comments/"

