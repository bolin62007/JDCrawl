# !/usr/bin/python3
# coding=utf-8

import threading
import queue
from lib.utility.subthread import SubThread
import conf

class ThreadPool(object):
    """线程池"""
    def __init__(self,crawl_func,save_func,workers,max_page = conf.max_page,max_thread = conf.max_threads):
        """
            @param crawl_func: 爬取函数
            @param save_func:  保存函数
            @param workers :  任务
            @param max_thread  :  最大线程数   
        """
        self.crawl_func = crawl_func
        self.save_func = save_func
        self.max_page = max_page
        
        self.result_queue = queue.Queue()
        
        current_thread = threading.currentThread()
        current_thread.setName("ThreadPool")
#         current_thread.setDaemon(True)
        
        #初始化任务以及子线程
        self.__init__workers(workers)
        self.__init__threads(max_thread)
        

#         current_thread.join(self.threads[-1])
            
    def __init__workers(self,workers):
        """创建人物队列"""
        self.worker_queue = queue.Queue()
        for i in workers:
            self.worker_queue.put(i)
            
    def __init__threads(self,max_thread):
        """创建子线程"""
        self.threads = []
        for i in range(max_thread):
            sub_thread = SubThread(
                            crawl_func = self.crawl_func,
                            save_func = self.save_func,
                            productIds_queue = self.worker_queue,
                            result_queue = self.result_queue,
                            max_page = self.max_page)
            self.threads.append(sub_thread)
            
            
    def start_all_threads(self):
        """启动所有线程"""
        for thread in self.threads:
            thread.start()
            
        for thread in self.threads:
            thread.join()
            
    
            
