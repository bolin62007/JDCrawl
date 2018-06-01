#! usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月23日

@author: qcymkxyc
'''

import threading
import conf



class SubThread(threading.Thread):
    """线程池中的线程"""
    def __init__(self,crawl_func,save_func,productIds_queue,result_queue,max_page  = None):
        """
            @param crawl_func:爬取函数
            @param save_func: 保存函数
            @param productIds_queue:  要爬取的商品ID的queue
            @param result_queue : 结果的queue
            @param max_page  :  爬取的最大页数     
        """
        super(SubThread,self).__init__()
        
        self.crawl_func = crawl_func
        self.save_func = save_func
        self.producIds_queue = productIds_queue
        self.max_page = max_page

        self.result_queue = result_queue
        
    def run(self):
        current_thread = threading.current_thread()
        while True:
            if not self.producIds_queue.empty():
                productId = self.producIds_queue.get()
            else:
                break;
            
            name_suffix = [save_way_name for save_way_name,save_way in conf.save_ways.items() if
                                         save_way == self.save_func][-1]
            print("子线程 {0} 开始爬取 ProductID : {1}".format(current_thread.getName(),productId))
            crawl_comments = self.crawl_func(productId,page_length = self.max_page)
            print("子线程 {0} 爬取ProductID ： {1} 完成".format(current_thread.getName(),productId))
            print("子线程 {0} 开始保存 productID : {1} 爬取的评论 ".format(current_thread.getName(),productId))
            self.save_func(conf.save_folder + str(productId) + "." + name_suffix,crawl_comments)
            print("子线程 {0} 保存 productID : {1} 完成".format(current_thread.getName(),productId))
            
            self.result_queue.put(crawl_comments)
        
        
