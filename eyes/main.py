from scrapy.cmdline import execute
import sys
import os
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))

# print(dirpath)
# 添加环境变量
sys.path.append(dirpath)

#切换到进入虚拟环境脚本路径
os.chdir(os.path.abspath(r".") + "\\eyesLib\\Scripts")
# 执行切入虚拟环境命令
os.system("activate")

# 切换到执行scrpay 框架工作路径
os.chdir(dirpath)
# source  F:\VsCodeWork\Scrapy\eyesLib\Scripts\activate
# print(os.path.abspath(r".") + "\\eyesLib")
# print(os.path.abspath(__file__))
# os.system(".\eyesLib\Scripts\activate")
# 启动爬虫,第三个参数为爬虫name
execute(['scrapy','crawl','thepaper'])
# print(os.path.abspath(__file__))
