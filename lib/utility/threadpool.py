# !/usr/bin/python3
# coding=utf-8

import queue
# from module.comment_crawl import CommentCrawl
from utility.subthread import SubThread

class ThreadPool(object):
    """线程池"""
    def __init__(self,func,workers,max_page = 2,max_thread = 10):
        """
            @param func: 要处理worker的函数
            @param workers :  任务
            @param max_thread  :  最大线程数   
        """
        self.func = func
        self.max_page = max_page
        
        self.result_queue = queue.Queue()
        
        #初始化任务以及子线程
        self.__init__workers(workers)
        self.__init__threads(max_thread)
        
        
            
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
                            func = self.func,
                            productIds_queue = self.worker_queue,
                            result_queue = self.result_queue,
                            max_page = self.max_page)
            self.threads.append(sub_thread)
            
            
    def start_all_threads(self):
        """启动所有线程"""
        for thread in self.threads:
            thread.start()
            
    
            
        
if __name__ == "__main__":
#     CommentCrawl = CommentCrawl()
#     threadp = ThreadPool(func = CommentCrawl.crawl_comment,workers = [0])
    pass
        
    