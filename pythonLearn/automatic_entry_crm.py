#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 10:29
# @Author  : Czech.Yuan
# @File    : automatic_entry_crm.py

from selenium import webdriver
import time
from collections import deque


def open_website_and_login(driver_chrome, content_text):
    driver_chrome.get('http://crm.fortruer.net/Login')
    driver_chrome.maximize_window()
    input_username = driver_chrome.find_element_by_name('userName')
    input_password = driver_chrome.find_element_by_name('password')
    input_username.send_keys('袁培根')
    input_password.send_keys('1234567')
    driver_chrome.find_element_by_class_name('submitButton').click()
    driver_chrome.implicitly_wait(2)
    # 打开 所有任务
    driver_chrome.find_element_by_xpath('//ul[@class="mItem mLvl1"]/li[2]').click()
    driver_chrome.implicitly_wait(2)
    # 切换到所有任务iframe
    driver_chrome.switch_to.frame('tabFrame_d7a9cbdb1e3bf2ad8617f97a1d9a9534')
    # 新增需求
    driver_chrome.find_element_by_xpath('//div[@class="btn-group"]').click()
    driver_chrome.find_element_by_xpath('//ul[@class="dropdown-menu"]/li[2]').click()
    time.sleep(2)
    # 关闭弹窗
    driver_chrome.switch_to.alert.dismiss()
    time.sleep(2)
    driver_chrome.switch_to.default_content()
    # 切换到 添加任务 iframe
    driver_chrome.switch_to.frame('xubox_iframe1')
    # 选择客户
    js_client_name = 'document.querySelector("#ClientNameText").innerHTML = "致真技术阿里云"'
    driver_chrome.execute_script(js_client_name)
    driver_chrome.find_element_by_id('ClientNameValidation').send_keys('致真技术阿里云')
    driver_chrome.find_element_by_id('ClientIDValidation').send_keys('38d31a89-6f63-47de-acb7-f3d995877066')
    # 问题类别
    js_data_type = '''document.querySelector("select[name='m.TaskItemDM.DataType']").value="400900"'''
    driver_chrome.execute_script(js_data_type)
    # 问题模块
    js_module_type = '''document.querySelector("select[name='m.TaskItemDM.ModuleType']").value="1005000"'''
    driver_chrome.execute_script(js_module_type)
    # 问题标题
    js_title = '''document.querySelector("input[name='m.TaskItemDM.ItemTitle']").value=`${new Date().getFullYear()}年${new Date().getMonth()+1}月${new Date().getDate()}日${new Date().getHours()}点工时记录`'''
    driver_chrome.execute_script(js_title)
    # 服务类别
    js_server_type = '''document.querySelector("select[name='m.TaskItemDM.ServerType']").value="200"'''
    driver_chrome.execute_script(js_server_type)
    # 转发人
    js_assignee_name = 'document.querySelector("#AssigneeName").innerHTML = "聂勇"'
    driver_chrome.execute_script(js_assignee_name)
    driver_chrome.find_element_by_id('AssigneeNameValidation').send_keys('聂勇')
    driver_chrome.find_element_by_id('AssigneeIDValidation').send_keys('04589dbf-616d-41e7-81c9-a2627a5c7515')
    # 工时
    js_work_time = '''document.querySelector("#CompleteWorkHours").value="8"'''
    driver_chrome.execute_script(js_work_time)
    js_content = f'''var CKEDITOR = window.CKEDITOR; CKEDITOR.instances.EditorOpCommentForward.setData("<p>转发给聂勇</p>"); CKEDITOR.instances.EditorMainContent.setData(`<img src='/UpLoadFiles/202101/08/100909781121.png' style="width:0.0001px!important;height:0.0001px!important" />{content_text}`);'''
    driver_chrome.execute_script(js_content)
    # 提交
    driver_chrome.find_element_by_xpath("//td[@class='opArea']/a").click()
    time.sleep(2)
    # 关闭浏览器
    driver_chrome.quit()


def tail_work_file(filename, n=4):
    lines = '<br>'.join(list(deque(open(filename, 'r', encoding='gbk'), n)))
    return lines


if __name__ == '__main__':
    # 读取当天工作日志
    content_text = tail_work_file(r'C:\Users\123\Desktop\Note.txt', 3)
    driver = webdriver.Chrome()
    open_website_and_login(driver, content_text)
