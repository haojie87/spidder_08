from selenium import webdriver

url = 'https://mail.qq.com/cgi-bin/loginpage'
browser = webdriver.Chrome()
browser.get(url)
# 1.切换到iframe 的子页面
iframe = browser.find_element_by_id('login_frame')
browser.switch_to.frame(iframe)

# 用户名+密码+登录按钮
browser.find_element_by_id('u').send_keys('1544239099')
browser.find_element_by_id('p').send_keys('TZH19901002002')
browser.find_element_by_id('login_button').click()