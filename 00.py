from selenium import webdriver
import pymysql

class GovSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        # 设置无界面模式
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=self.options)
        self.db = pymysql.connect(
            'localhost','root','123456','govdb',charset='utf8'
        )
        self.cursor = self.db.cursor()
        # 用于executemany([(),(),()])
        self.province = []
        self.city = []
        self.county = []

    # 提取数据
    def get_data(self):
        self.browser.get(self.url)
        node = self.browser.find_element_by_partial_link_text('县以上行政区划代码')
        # 先判断此节点之前是否抓取过
        link = node.get_attribute('href')
        sel = 'select url from version where url=%s'
        result = self.cursor.execute(sel,[link])
        if not result:
            # 1.抓取
            self.get_code(node)
            # 2.把此链接存入数据库version表中
            ins = 'insert into version values(%s)'
            self.cursor.execute(ins,[link])
            self.db.commit()
        else:
            print('未更新')

    # 具体抓取数据
    def get_code(self,node):
        node.click()
        # 切换句柄
        all = self.browser.window_handles
        self.browser.switch_to.window(all[1])
        # 提取数据
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            name = tr.text.split()[1]
            code = tr.text.split()[0]
            print(name,code)
            # 上海市 上海市 浦东新区
            if code[-4:] == '0000':
                self.province.append((name,code))
                # 把4个直辖市添加到city表
                if code[:2] in ['11','12','31','50']:
                    self.city.append((name,code,code))

            elif code[-2:] == '00':
                pcode = code[:2] + '0000'
                self.city.append((name,code,pcode))
            else:
                if code[:2] in ['11','12','31','50']:
                    ccode = code[:2] + '0000'
                else:
                    ccode = code[:4] + '00'
                self.county.append((name,code,ccode))

        self.insert_mysql()

    def insert_mysql(self):
        # 1.先清除原有数据
        del1 = 'delete from province'
        del2 = 'delete from city'
        del3 = 'delete from county'
        self.cursor.execute(del1)
        self.cursor.execute(del2)
        self.cursor.execute(del3)
        self.db.commit()
        # 2.插入新的数据
        ins1 = 'insert into province values(%s,%s)'
        ins2 = 'insert into city values(%s,%s,%s)'
        ins3 = 'insert into county values(%s,%s,%s)'
        self.cursor.executemany(ins1,self.province)
        self.cursor.executemany(ins2,self.city)
        self.cursor.executemany(ins3,self.county)
        self.db.commit()

    def run(self):
        self.get_data()
        self.browser.quit()

if __name__ == '__main__':
    spider = GovSpider()
    spider.run()






























