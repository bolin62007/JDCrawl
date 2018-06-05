#! /usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月17日

@author: leonlee
'''
from lib.module.comment_crawl import CommentCrawl
import argparse
import conf
import sys

comment_crawl = CommentCrawl()
    
def init_parse():
    """初始化命令行"""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='京东评论爬虫小工具',dest = "sub_command")
    
    ###################################################################################
    #    单个商品
    ##################################################################################
    def crawl_single_func(args):
        comment_crawl.crawl_comment(
                            productId = args.productID,
                            page_length = args.pages, 
                            save_way = args.save_way
        )
        
    
    crawl_single_parser = subparsers.add_parser('crawl-single', help = '爬取单个商品评论')
    crawl_single_parser.add_argument('productID',help='爬取的商品ID',type = int)
    crawl_single_parser.add_argument('--pages',help = "爬取的评论页数",default = conf.max_page)
    crawl_single_parser.add_argument("-s","--save-way",
                                     help = "保存方式,共有三种方式，分别为mongodb，txt，csv，默认为保存为csv格式",
                                     default = "csv",
                                     choices = conf.save_ways.keys())
    crawl_single_parser.set_defaults(func = crawl_single_func)
    
    ######################################################################################
    #    多个商品
    ######################################################################################
    def crawl_item_func(args):
        print(args)
        comment_crawl.crawl_from_itemlist(
                            items_url = args.url, 
                            max_page = args.pages,
                            save_way = args.save_way,
                            max_thread = args.threads
                            )
        
    crawl_list_parser = subparsers.add_parser("crawl-list",help = "爬取多个评论")
    crawl_list_parser.add_argument("url",help = "url")
    crawl_list_parser.add_argument('--pages',help = "爬取的评论页数",default = conf.max_page)
    crawl_list_parser.add_argument("-s","--save-way",
                                     help = "保存方式,共有三种方式，分别为mongodb，txt，csv，默认为保存为csv格式",
                                     default = "csv",
                                     choices = conf.save_ways.keys())
    crawl_list_parser.add_argument("-t","--threads",
                                   help = "线程池中的线程数,默认为{}".format(conf.max_threads),
                                   default = conf.max_threads)
    
    crawl_list_parser.set_defaults(func = crawl_item_func)
    
    return parser.parse_args()

def main():
    args = init_parse()
    args.func(args)
    sys.exit()
    

if __name__ == "__main__":
    main()

