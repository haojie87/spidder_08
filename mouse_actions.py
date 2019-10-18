'''点击百度页面-设置-高级搜索'''

from selenium import webdriver
from selenium.webdriver import ActionChains

browser  = webdriver.Chrome()
browser.get('http://www.baidu.com')

node = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
# 移动鼠标到设置
# mouse = ActionChains(browser)
# mouse.move_to_element(node)
# mouse.perform()
# 相当于:
ActionChains(browser).move_to_element(node).perform()

browser.find_element_by_link_text('高级搜索').click()