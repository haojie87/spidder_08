import requests
import execjs
import re

class BaiduTranlate(object):
    def __init__(self):
        self.get_url= 'https://fanyi.baidu.com/'
        self.post_url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.headers = {
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "cache-control":"max-age=0",
            "cookie":"BIDUPSID=C2D88AA0D52C8427FFEE1DC2987C937B; BAIDUID=234B9C0F5C463F669EDFCC177CEE71E3:FG=1; PSTM=1564538946; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; H_PS_PSSID=1430_21123_29567_29699_29220; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1571119621,1571381226; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1571386112; __yjsv5_shitong=1.0_7_05d209d2c8c4cb8fc67f799c74ae8dabb17b_300_1571386112145_43.254.90.134_48d9af16; yjs_js_security_passport=bfd431dce2c604469ec817b4fd7e346564673489_1571386130_js",
            "upgrade-insecure-requests":"1",
            "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1"
            }

    # 获取gtk和token
    def get_gtk_token(self):
        html = requests.get(url=self.get_url,headers=self.headers).text
        # 获取gtk
        p=re.compile("window\.gtk = '(.*?)'",re.S)
        gtk = p.findall(html)[0]
        print(gtk)
        # 获取token
        p=re.compile("token: '(.*?)'",re.S)
        token = p.findall(html)[0]

        return gtk, token

    # 获取sign
    def get_sign(self,word,gtk):
        with open('translate.js','r') as f:
            data=f.read()
        # 执行js
        jsobj = execjs.compile(data)
        sign = jsobj.eval('e("{}","{}")').format(word,gtk)
        return sign

    def run(self):
        word = input('请输入要翻译的单词:')
        gtk,token = self.get_gtk_token()
        sign = self.get_sign(word,gtk)
        formdata= {
                "from":"en",
                "to":"zh",
                "query":word,
                "transtype":"realtime",
                "simple_means_flag":"3",
                "sign":sign,
                "token":token,
                }
        html = requests.post(self.post_url, data=formdata, headers=self.headers).json()
        # result = html['trans_result']['data'][0]['dst']
        print(html)

if __name__ == '__main__':
    spider = BaiduTranlate()
    spider.run()

