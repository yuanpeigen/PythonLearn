import requests
from bs4 import BeautifulSoup

# 目标页面url地址
url = 'http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-1-2.html'
page_num = 1


def print_game_name(url):
    # 发送请求，r为页面响应
    r = requests.get(url)

    # r.text获取页面代码
    # 使用lxml解析页面代码
    soup = BeautifulSoup(r.text, 'lxml')

    # 两次定位，先找到整个信息区域
    info_list = soup.find_all(attrs={'class': 'ptlist ptlist-pc'})

    # 在此区域内获取游戏名，find_all返回的是list
    tit_list = info_list[0].find_all(attrs={'class': 'tit'})

    # 遍历获取游戏名
    # .text可获取文本内容，替换掉文章中的换行符
    for title in tit_list:
        print(title.text.replace('\n', ''))


# 取前5页数据
def get_five_page():
    for i in range(page_num, 6):
        page_url = f'{url}?page={i}'
        print(f'++++++++++++++++++++++第{i}页++++++++++++++++++++++')
        print_game_name(page_url)


if __name__ == '__main__':
    get_five_page()
