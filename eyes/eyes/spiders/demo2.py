# from playwright.sync_api import sync_playwright, Playwright
# from bs4 import BeautifulSoup

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)          # 启动 chromium 浏览器
#     page = browser.new_page()              # 打开一个标签页
#     page.goto("https://www.thepaper.cn/")     # 打开百度地址
#     print(page.title())                    # 打印当前页面title
#     # page.pause()
#     # 通过playwright 加载动态页面 并通过定位器获取热搜模块 内容 返回html
#     hotHtml = page.locator('xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]').inner_html()

#     # 通过 BeautifulSoup 解析 热搜html
#     soup = BeautifulSoup(hotHtml, 'html.parser')
#     # 解析html 内容取出所有a 标签对象
#     hotA = soup.find_all('a')

#     for  line in hotA :
#         #打印a 标签所有链接 href 属性
#         print(line.get('href'))
#         #打印a 标签所有内容
#         print(line.text)

#     # print(soup.p['class'])
#     # hotnew  = page.locator('div:nth-child(4) > .index_content___Uhtm').all_inner_texts()
#     # hotnew2 = page.get_by_role("listitem")
#     # # text = hotnew.inner_text()# 获取元素内部的文本
#     # # element = hotnew.text_content()
#     # for row in page.get_by_role("listitem").all():
#     #     print(row.text_content())'https://www.thepaper.cn/newsDetail_forward_30502801'
#     #     print()
#     # # print(text)
#     # print(hotHtml)
#     # print(hotnew2)
#     browser.close()                        # 关闭浏览器对象