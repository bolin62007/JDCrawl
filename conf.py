#!/usr/bin/python3
#coding=utf8
'''
Created on 2018年5月17日

@author: leonlee
'''
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