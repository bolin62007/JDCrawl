#!usr/bin/python3
#coding=utf-8
'''
Created on 2018年5月17日

@author: leonlee
'''
import conf
import re
import json
import requests

class CommentCrawl(object):
    """评论爬取
    """
    def __init__(self):
        pass
        
    @staticmethod
    def crawl_page(params):
        """爬取页面
            @param params:参数 
            @return: 页面的字符串形式
        """
        response = requests.get(conf.base_url,params)
        return response.text
    
    
    def crawl_comment(self,productId,page = 0):
        """爬取评论
            @param productId: 商品ID
            @param page : 评论的第几页  
            @return: 评论的dict形式
        """
        #设置参数
        comment_param = conf.comment_crawl_params
        comment_param["productId"] = productId
        comment_param["page"] = page
        
        #正则匹配
        response_text = CommentCrawl.crawl_page(comment_param)
        pattern = re.compile(conf.crawl_comment_rule, re.S)
        match_result = pattern.findall(response_text)
        match_result = [json.loads(x) for x in match_result]
        
        return match_result
        
        
    def get_productId(self,items_url = conf.items_url):
        """根据商品列表取得商品的ID
            @param items_url : 商品列表的url 
            @return: 商品的字典形式{商品ID ： 商品名} 
        """
        response = requests.get(url = items_url)
        match_rule = "<div class=\"p-name\".*?(href.*?)</em>"
        match_result = re.findall(match_rule,response.text, re.S)
            
        products = dict()
        for product_str in match_result[1:]:
            product_id = re.findall("\/(\d+)\.",product_str,re.S)[-1]
            product_id = int(product_id)
            
            product_name = re.findall("<em>(.*)",product_str,re.S)[0]
            product_name = product_name.strip()
            
            products[product_id] = product_name
            
        return  products
    
    def crawl_from_itemlist(self,items_url = conf.items_url,max_page = None):
        """"""
        product_Ids = self.get_productId(items_url);
        all_comments = list()
        
        count = 0
        for product_Id in product_Ids.keys():
            count += 1
            if count == 10:
                break
            page = 0;
            while True:
                comments = self.crawl_comment(product_Id, page)
                all_comments.extend(comments)
                if len(comments) == 0 or page > max_page:
                    break
                page += 1
        return all_comments
        
if __name__ == "__main__":
    r = requests.get("https://list.jd.com/list.html?cat=1713,3287,3804&go=0")
    print(r.text)

        
        

    