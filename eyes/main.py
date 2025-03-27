from scrapy.cmdline import execute
import sys
import os
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
print(1111)

print(dirpath)
# 添加环境变量
sys.path.append(dirpath)

#切换工作路径
os.chdir(dirpath)
os.system("F://VsCodeWork//Scrapy//eyesLib//Scripts//activate")
# source  F:\VsCodeWork\Scrapy\eyesLib\Scripts\activate

# os.system(".\eyesLib\Scripts\activate")
# 启动爬虫,第三个参数为爬虫name
execute(['scrapy','crawl','demo'])
# print(os.path.abspath(__file__))
