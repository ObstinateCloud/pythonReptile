#### scrapy 是一个为了爬取网站数据，提取机构型数据而编写的应用框架，可以应用在:包括数据挖掘、信息处理或存储历史数据等一系列的程序中
#### 1.安装 pip install scrapy
#### 2.使用scrapy创建项目： scrapy startproject 项目名
#### 3.项目文件写在spiders目录下
#### 4.创建爬虫文件：scrapy genspider 文件名 要爬取的网页 
eg:scrapy genspider baidu http://www.baidu.com
#### 5.运行：scrapy crawl 爬虫名字
eg:scrapy crawl baidu
#### 6.scarpy项目
项目名
  项目名称
     spiders文件夹(存储爬虫文件)
        init
     init
     items  定义数据结构
     middlewares