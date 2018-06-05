# JDCrawl
京东评论爬取的小工具,你可以用来作推荐系统和情感分析的练习数据
该工具一共有两个小功能：

```

	usage: JDCrawl.py [-h] {crawl-single,crawl-list} ...
	
	positional arguments:
	  {crawl-single,crawl-list}
	                        京东评论爬虫小工具
	    crawl-single        爬取单个商品评论
	    crawl-list          爬取多个评论
	
	optional arguments:
	  -h, --help            show this help message and exit
	
```
	
	* 爬取单个商品
		你可以通过执行：
		```
			./JDCrawl.py crawl-single 商品ID
		```
		或
		``` 
			python3 ./JDCrawl.py crawl-single 商品ID
		```
		爬取商品，执行后会程序会在该目录下新建一个comment文件夹，存储爬取数据，文件名为商品ID
		
	* 爬取一个页面上的商品列表
	