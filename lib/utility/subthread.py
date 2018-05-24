#! usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月23日

@author: qcymkxyc
'''

import threading

class SubThread(threading.Thread):
    """线程池中的线程"""
    def __init__(self,func,productIds_queue,result_queue,max_page  = None):
        super(SubThread,self).__init__()
        
        self.func = func
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
            print("子线程 {0} 开始爬取 ProductID : {1}".format(current_thread.getName(),productId))
            crawl_comments = self.func(productId,self.max_page)
            self.result_queue.put(crawl_comments)
        
        
