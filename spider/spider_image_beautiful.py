import os
import random
import requests
from bs4 import BeautifulSoup
import datetime
from concurrent.futures import ThreadPoolExecutor

# 图片保存路径
file_path = './image/girl/'
# 最大页数
max_pageNum = 175
# 随机使用UserAgent
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


class SpiderImage:

    def __init__(self, total_page):
        # 获取页数
        self.total_page = total_page
        # 目标url
        self.url = 'https://pic.netbian.com'
        self.headers = {
            'referer': self.url,
            'user-agent': user_agent_list[0],
        }
        self.start_time = None
        self.total_image = 0

    def start_work(self):
        if self.total_page >= max_pageNum:
            print('超出最大页数！')
            return
        # 记录当前时间
        self.start_time = datetime.datetime.now()
        for i in range(1, self.total_page + 1):
            print(f'第{i}页\n\n')
            # 更新随机抽选的UserAgent
            self.headers['user-agent'] = random.choice(user_agent_list)
            page_url = self.get_page_url(i)
            self.get_html(page_url)

    def get_page_url(self, current_page_num):
        home_url = self.url + '/4kmeinv/index'
        return home_url + (f'_{current_page_num}' if current_page_num > 1 else '') + '.html'

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'gbk'  # 网页编码gbk
        self.get_image_url(response.text)

    def get_image_url(self, html_text):
        soup = BeautifulSoup(html_text, 'lxml')
        soup_img = soup.find_all('div', attrs={'class': 'slist'})[0].find_all('img')
        image_info_list = []
        for img in soup_img:
            name = img['alt'].replace(' ', '')  # 去除所有空格
            image_info_list.append({'name': name[0:name.find('4k')], 'url': self.url + img['src']})
        self.batch_download(image_info_list)

    def batch_download(self, image_info_list):
        self.total_image += len(image_info_list)
        for imag_info in image_info_list:
            self.download_image(imag_info['url'], imag_info['name'])

    def download_image(self, url, name):
        # 创建目录
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        print(f'{name} {url}\n')
        response_image = requests.get(url, headers=self.headers)
        with open(file_path + name + '.jpg', 'wb') as f:
            f.write(response_image.content)


if __name__ == '__main__':
    total_page = 3
    spider = SpiderImage(total_page)
    # 启用多线程
    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(spider.start_work())
    # 时间花费
    time_spent = (datetime.datetime.now() - spider.start_time).total_seconds()
    print(f'下载{total_page}页图片,共计{spider.total_image}张，用时：{time_spent}s')
