from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
driver.get('http://www.python3.vip/doc/tutorial/python/code/sample1.html')

# 根据 tag name 选择元素，返回的是 一个列表
# 里面 都是 tag 名为 div 的元素对应的 WebElement对象
elements = driver.find_element_by_css_selector('#searchtext')

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)



{% include sharepost.html %}