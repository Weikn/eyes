from playwright.sync_api import sync_playwright, Playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)          # 启动 chromium 浏览器
    page = browser.new_page()              # 打开一个标签页
    page.goto("https://www.thepaper.cn/")     # 打开百度地址
    print(page.title())                    # 打印当前页面title
    page.pause()
    hotnew = page.locator('div:nth-child(4) > .index_content___Uhtm').inner_html()
    # text = hotnew.inner_text()# 获取元素内部的文本
    # element = hotnew.text_content()
    # print(text)
    print(hotnew)
    browser.close()                        # 关闭浏览器对象