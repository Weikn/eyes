# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

## 管道 在这里进行定义存储 存储到MySQL  需要写 pdbc
class EyesPipeline:
    def process_item(self, item, spider):
        print("EyesPipeline")
        print(spider.name)
        print(item)
        return item


class HotSearchPipeline:
    def open_spider(self, spider):
        db = "DB"
        host = ""
        port = 3306
        user = 'root'
        passwd = "smart@123"
        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()
    
    
    
    
    def close_spider(self, spider):
#第五步 提交数据库执行
        # pass
        self.db_conn.commit()
        self.db_conn.close()


    def insert_db(self, item):
        values = (
            item['date'][0],
            # "",
            # "",
            item['auther'][0],
            item['content'][0],
        )
        print("Insert 成功了")
        sql = 'INSERT INTO HotSearch(date,auther,content) VALUES(%s,%s,%s)'
#第四步 用游标执行数据库命令
        self.db_cur.execute(sql, values)
        # self.db_conn.commit()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host="aweikn.top",
    #         db="DB",
    #         user="root",
    #         passwd="smart@123",
    #         use_unicode=True)
    #     self.cursor = self.connect.cursor()

    # def process_item(self, item, spider):
    #     if spider.name == 'thepaper':
    #         # self.cursor.execute(
    #         #     'INSERT INTO HotSearch VALUES (,title,auther,source,content,url,types,date) values (%s,%s,%s,%s,%s,%s,%s)',
    #         #     (item['title'],item['auther'],item['source'],item['content'],item['url'],
    #         #      item['types'],item['date']))
    #         self.cursor.execute(
    #             'INSERT INTO HotSearch  (auther,content,date) values (%s,%s,%s,)',(item['auther'],item['content'],item['date']))
    #         self.connect.commit()
    #     print("HotSearchPipeline")
    #     print(spider.name)
    #     print(item)
    #     return item



# class BgmspiderPipeline(object):
#     def __init__(self):
#         self.connect = pymysql.connect(
#             host=settings.MYSQL_HOST,
#             db=settings.MYSQL_DBNAME,
#             user=settings.MYSQL_USER,
#             passwd=settings.MYSQL_PASSWD,
#             use_unicode=True)
#         self.cursor = self.connect.cursor()
 
#     def process_item(self, item, spider):
#         if spider.name == 'bgm':
#             self.cursor.execute(
#                 'insert ignore into bgm (bgm_name,bgm_cat,bgm_tag,bgm_time,bgm_music,bgm_link,bgm_img) values (%s,%s,%s,%s,%s,%s,%s)',
#                 (item['bgm_name'],item['bgm_cat'],item['bgm_tag'],item['bgm_time'],item['bgm_music'],
#                  item['bgm_link'],item['bgm_img']))
#             self.connect.commit()
#         return item