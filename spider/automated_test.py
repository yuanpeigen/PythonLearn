'''Web自动化测试，简单演示 '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 在Chrome中打开百度首页
def openChrome(driver_chrome):
    driver_chrome.get('https://www.baidu.com')
    # 浏览器窗口最大化
    driver_chrome.maximize_window()
    # 通过id定位搜索框
    search_input = driver_chrome.find_element_by_id('kw')
    # 在搜索框中输入关键字
    search_input.send_keys('python3')
    # 按回车
    search_input.send_keys(Keys.ENTER)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    openChrome(driver)
