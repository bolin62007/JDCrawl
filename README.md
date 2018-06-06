# JDCrawl
用线程池实现的京东商品评论爬取小工具,你可以用来作推荐系统和情感分析的练习数据集
## 基本用法
    
* **爬取单个商品**：

```
	./JDCrawl.py crawl-single 商品ID
```
    脚本会将爬取的商品评论储存在comments文件夹下
        
* **爬取一个页面上所有商品评论**：
```
    ./JDCrawl.py crawl-list 页面url
```
    程序会检测该url下所有的商品ID，默认用10个子线程爬取，并将爬取的所有商品评论存储在comments文件夹下
## 更多
	1. 指定爬取页数
```
    ./JDCrawl crawl-single --pages 页数
```
	2. 指定存储方式
```
    ./JDCrawl crawl-list -s 存储方式
```
    存储方式一共有3中，分别为txt，mongodb，csv，默认为csv
    3. 指定线程数
```
    ./JDCrawl crawl-list -t 线程数
```
    线程默认为10个线程，可以根据需要更改