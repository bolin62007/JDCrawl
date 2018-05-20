#! /usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月17日

@author: leonlee
'''
from module.comment_crawl import CommentCrawl
import requests

def main():
    comment_crawl = CommentCrawl()
#     comment_crawl.crawl_comment(11242112, 1)
#     r = comment_crawl.crawl_comment(27555188739,page = 1)
    r = comment_crawl.crawl_from_itemlist(max_page = 2)
#     
    for i in r:
        print(i)
#     r = comment_crawl.get_productId()
#     print(len(r))
#     for i,j in r.items():
#         print(i,j)
#     r = requests.get("https://list.jd.com/list.html?cat=1713,3287,3804&go=0")
#     print(r.text)
    

if __name__ == "__main__":
    main()