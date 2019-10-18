'''设置无界面模式(无头模式)'''

from selenium import webdriver

# 1.创建功能对象
options=webdriver.ChromeOptions()

# 2.添加一个无头参数
options.add_argument('--headless')

# 3.创建浏览器对象
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')
browser.quit()