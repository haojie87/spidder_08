import requests
import execjs
import re

class BaiduTranslate(object):
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/'
        self.post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "BAIDUID=11DF7A4BB8E40E7BD65C50336A33AFB4:FG=1; BIDUPSID=11DF7A4BB8E40E7BD65C50336A33AFB4; PSTM=1570851270; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; H_PS_PSSID=1435_21110_29567_29220_26350; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1571111905,1571381206; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1571385691; __yjsv5_shitong=1.0_7_bf58e74149ee1c34157a80ec6c0b6d9674d2_300_1571385689738_43.254.90.134_9bea61e6; yjs_js_security_passport=b25d1ff3558c35981bf191ffc555542b875eea76_1571385690_js",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        }

    # 获取gtk和token
    def get_gtk_token(self):
        html = requests.get(url=self.get_url,headers=self.headers).text
        # 获取gtk
        p = re.compile("window\.gtk = '(.*?)'",re.S)
        gtk = p.findall(html)[0]
        # 获取token
        p = re.compile("token: '(.*?)'", re.S)
        token = p.findall(html)[0]

        return gtk,token

    # 获取sign
    def get_sign(self,word,gtk):
        with open('translate.js','r') as f:
            data = f.read()
        # 执行js
        jsobj = execjs.compile(data)
        sign = jsobj.eval('e("{}","{}")'.format(word,gtk))

        return sign

    def run(self):
        word = input('请输入要翻译的单词:')
        gtk,token = self.get_gtk_token()
        sign = self.get_sign(word,gtk)
        formdata = {
            "from": "auto",
            "to": "auto",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
        }
        html = requests.post(
            url=self.post_url,
            data=formdata,
            headers=self.headers
        ).json()
        result = html['trans_result']['data'][0]['dst']
        print(result)

if __name__ == '__main__':
    spider = BaiduTranslate()
    spider.run()














