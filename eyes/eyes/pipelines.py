# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
import logging
import json
import os
## 管道 在这里进行定义存储 存储到MySQL  需要写 pdbc
class EyesPipeline:
    def process_item(self, item, spider):
        logging.debug("EyesPipeline")
        return item




class HotSearchPipeline:
    
    def __init__(self):
        logging.debug("HotSearchPipeline init")
        # 声明一个字典
        dbparams= {}
        # 读取db 配置文件 db.json 
        with open(os.path.dirname(os.path.abspath(__file__))+ "/" +"db.json", "r") as f:
            dbparams = json.load(f)
        # 配置文件生成字典
        dbparams["cursorclass"] = cursors.DictCursor
        #初始化数据库连接池，参数1是mysql的驱动，参数2是连接mysql的配置信息
        self.db_pool = adbapi.ConnectionPool('pymysql', **dbparams)
        #sql语言的空值
        self._sql = None
    


    @property
    def sql(self):
        if not self._sql:
            self._sql = 'INSERT INTO HotSearch(date,auther,content,title,url,source,type,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
            return self._sql
        return self._sql
 
    def process_item(self, item, spider):
        #操作数据，将数据写入数据库
        #如果是同步写入的话，使用的是cursor.execute(),commit()
        #异步存储的方式：函数方式pool.map(self.insert_db,[1,2])
        logging.info(item)
        query = self.db_pool.runInteraction(self.insert_db,item)
        query.addErrback(self.handle_error, item, spider)
    def insert_db(self,cursor, item):
        logging.debug("--------insert Db--------")
        values = (
            item['date'],
            item['auther'],
            item['content'],
            item['title'],
            item['url'],
            item['source'],
            item['type'],
            item['status'],
        )
        logging.debug("--------Insert success--------")
        cursor.execute(self.sql, values)
    def handle_error(self,error,item,spider):
        logging.error('='*10 + "error" + '='*10)
        logging.error(error)
        logging.error('=' * 10 + "error" + '=' * 10)
        
