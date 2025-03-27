#  poject  infols

#  python -m venv eyesLib

#  .\eyesLib\Scripts\activate 


locator.inner_html()  #获取某个元素的HTML
locator.text_content() #用来获取某个元素内所有文本内容，包含子元素内容，隐藏元素也能获取。返回值不会被格式化,返回值依赖于代码的内容
locator.inner_text()    #的返回值会被格式化,inner_text()返回的值, 依赖于页面的显示, 
locator.count()  #获取元素个数
all_inner_texts() 和 all_text_contents()  #也是用于获取页面上的文本，但是返回的是list列表
