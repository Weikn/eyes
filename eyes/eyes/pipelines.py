# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

## 管道 在这里进行定义存储 存储到MySQL  需要写 pdbc
class EyesPipeline:
    def process_item(self, item, spider):
        print("EyesPipeline")
        print(spider.name)
        print(item)
        return item


class HotSearchPipeline:
    
    
    def __init__(self):
        dbparams = {
            'host': '',
            'port': 3306,
            'user': 'root',
            'password': 'smart@123',
            'database': 'DB',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor  # 指定cursor的类
        }
    #初始化数据库连接池，参数1是mysql的驱动，参数2是连接mysql的配置信息
        self.db_pool = adbapi.ConnectionPool('pymysql', **dbparams)
    #sql语言的空值
        self._sql = None
    


    @property
    def sql(self):
        if not self._sql:
            self._sql = 'INSERT INTO HotSearch(date,auther,content) VALUES(%s,%s,%s)'
            return self._sql
        return self._sql
 
    def process_item(self, item, spider):
        #操作数据，将数据写入数据库
        #如果是同步写入的话，使用的是cursor.execute(),commit()
        #异步存储的方式：函数方式pool.map(self.insert_db,[1,2])
        query = self.db_pool.runInteraction(self.insert_db,item)
        query.addErrback(self.handle_error, item, spider)
    def insert_db(self,cursor, item):
        print("insert")
        values = (
            item['date'],
            item['auther'],
            item['content'],
        )
        print("Insert 成功了")
        cursor.execute(self.sql, values)
    def handle_error(self,error,item,spider):
        print('='*10 + "error" + '='*10)
        print(error)
        print('=' * 10 + "error" + '=' * 10)
