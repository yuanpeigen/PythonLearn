import requests
from bs4 import BeautifulSoup

target_url_catLog = 'https://book.qidian.com/info/114559#Catalog'


class Book:
    def __init__(self):
        self.target_url = target_url_catLog
        self.num = 0
        self.urls = []

    # 获取内容
    @staticmethod
    def getContents(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        book_content = soup.find_all('div', attrs={'class': 'read-content j_readContent'})
        print('内容：', book_content[0].text)
        return book_content[0].text

    # 获取每一章节url
    def getContentDownloadUrl(self):
        r = requests.get(target_url_catLog)
        soup = BeautifulSoup(r.text, 'lxml')
        soup_p = soup.find_all('div', attrs={'class': 'volume'})
        soup_a = soup_p[0].find_all('a')[1:]
        self.urls = list(map(lambda x: self.formatContentUrl(x.get('href')), soup_a))
        self.num = len(self.urls)

    # 写入文件
    @staticmethod
    def write(text):
        with open('book.txt', 'a', encoding='utf-8') as f:
            f.write(text.strip().replace('\n', '').replace('\r', ''))
            f.write('\n\n')  # 换两行

    # 格式化Url
    @staticmethod
    def formatContentUrl(download_url):
        return f'https:{download_url}'

    # 开始下载
    def startDownload(self):
        self.getContentDownloadUrl()
        print('<<<<<<<<<开始下载>>>>>>>>>')
        for i in range(self.num):
            print(f'<<<<<<<<<正在下载第{i + 1}页>>>>>>>>>')
            self.write(self.getContents(self.urls[i]))
        print('<<<<<<<<<下载完成>>>>>>>>>')


if __name__ == '__main__':
    book = Book()
    book.startDownload()
