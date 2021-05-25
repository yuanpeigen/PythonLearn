import requests
from bs4 import BeautifulSoup

test_url = "https://www.baidu.com"
wb_url = "https://www.weibo.com"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


def print_html(url):
    # 添加headers
    r = requests.get(url, headers=headers)
    # 返回请求状态码，200即为请求成功
    print(r.status_code)
    r.encoding = 'utf-8'
    # 返回页面代码
    print(r.text)


# post请求
def post_request(url):
    # 保持会话
    # 新建一个session对象
    sess = requests.session()
    # 先完成登录
    data = {'user': 'abc', 'password': '123'}
    r = requests.post(url, data=data, headers=headers)
    # 对于特定类型的请求，如Ajax请求返回的json数据
    print(r.json())
    # 然后再在这个会话下去访问其他的网址
    sess.get('other url')


# BeautifulSoup的使用
def trainingBeautifulSoup():
    html = '''<html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <p class="story">...</p>'''
    # 选用lxml解析器来解析
    soup = BeautifulSoup(html, 'lxml')
    # 获取标题标签
    print(soup.title)
    # 获取文本
    print(soup.title.text)
    # 通过标签定位
    print(soup.find_all('a'))
    # 通过属性定位
    print(soup.find_all(attrs={'id': 'link1'}))
    # 标签加属性定位
    print(soup.find_all('a', id='link1'))


if __name__ == '__main__':
    # print_html(test_url)
    # post_request(wb_url)
    trainingBeautifulSoup()
