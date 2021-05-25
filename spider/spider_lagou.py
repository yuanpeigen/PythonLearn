import requests


class Config:
    # 搜索关键词
    kd = '数据分析'
    referer = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': referer,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }


class Spider:

    def __init__(self, kd=Config.kd):
        self.kd = kd
        self.url = Config.referer
        self.api = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'

        # 必须先请求referer网址
        self.sess = requests.session()
        print(requests.get(self.url).text)
        # self.sess.get(self.url, headers=Config.headers)

    def get_position(self, pn):
        data = {
            'first': 'true',
            'pn': str(pn),
            'kd': self.kd
        }
        # 向API发起POST请求
        r = self.sess.post(self.api, headers=Config.headers, data=data)
        # 直接.json()解析数据
        print(r.json())
        return r.json()['content']['positionResult']['result']

    def engine(self, total_pn):
        for pn in range(1, total_pn + 1):
            results = self.get_position(pn)
            for pos in results:
                print(pos['positionName'], pos['companyShortName'], pos['workYear'], pos['salary'])


if __name__ == '__main__':
    lagou = Spider()
    lagou.engine(10)
