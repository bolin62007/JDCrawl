#! /usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月17日

@author: leonlee
'''
from lib.module.comment_crawl import CommentCrawl
import sys
import argparse
import conf

    
def init_parse():
    """初始化命令行"""
    parser = argparse.ArgumentParser()
    
    subparsers = parser.add_subparsers(help='commands')
    
    
    crawl_single_parser = subparsers.add_parser('crawl-single', help = '爬取单个商品评论')
    crawl_single_parser.add_argument('productID',help='爬取的商品ID',type = int)
    crawl_single_parser.add_argument('--pages',help = "爬取的评论页数",default = conf.max_page)
    crawl_single_parser.add_argument("-s","--save-way",help = "保存方式,默认为保存为csv格式",default = "csv")
    
    crawl_list_parser = subparsers.add_parser("crawl-list",help = "爬取多个评论")
    crawl_list_parser.add_argument("url",help = "url地址")
    crawl_list_parser.add_argument("-t","--threads",help = "线程池中的线程数",default = conf.max_threads)
    crawl_list_parser.add_argument("-s","--save-way",help = "保存方式",default = "csv")
    

    return parser.parse_args()

def main():
    args = init_parse()
    
    
    comment_crawl = CommentCrawl()
    

if __name__ == "__main__":
    init_parse()
#     main()