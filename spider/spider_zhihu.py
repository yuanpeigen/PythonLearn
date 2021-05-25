#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 16:47
# @Author  : Czech.Yuan
# @File    : spider_zhihu.py

import re
import urllib.request

import requests
import json
import os
from os.path import basename
from urllib.parse import urlsplit

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br'
}
txt = 'pretty_pic'


def get_image_url(title=txt, qid='379425092'):
    answers_url = 'https://www.zhihu.com/api/v4/questions/' + str(
        qid) + '/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset={}&limit=10&sort_by=default&platform=desktop'
    offset = 0
    session = requests.Session()
    while True:
        page = session.get(answers_url.format(offset), headers=headers)
        json_text = json.loads(page.text)
        answers = json_text['data']
        if not answers:
            next_step = input('获取图片完成，是否开始下载？[YES] [NO]\n')
            if next_step == 'yes':
                read_file(title)
            return
        offset += 10
        pic_re = re.compile('data-original="(.*?)"', re.S)
        for answer in answers:
            tmp_list = []
            pic_urls = re.findall(pic_re, answer['content'])
            for item in pic_urls:
                pic_url = item.split('?')[0]
                # 去重复
                if pic_url not in tmp_list:
                    tmp_list.append(pic_url)
            write_file(title, tmp_list)


def write_file(title, pic_urls):
    if len(pic_urls) == 0:
        return
    file_name = title + '.txt'
    f = open(file_name, 'a')
    for pic_url in pic_urls:
        if pic_url.endswith('r.jpg'):
            print('写入 {}'.format(pic_url))
            f.write(pic_url + '\n')
    f.close()


def read_file(title):
    file_name = title + '.txt'
    pic_urls = []
    # 判断文件是否存在
    if not os.path.exists(file_name):
        return pic_urls
    with open(file_name, 'r') as f:
        for line in f:
            url = line.replace('\n', '')
            if url not in pic_urls:
                pic_urls.append(url)
    print('文件中共有{}个不重复的 URL'.format(len(pic_urls)))
    download_pic(pic_urls, title)


def download_pic(pic_urls, title):
    # 创建文件夹
    if not os.path.exists(title):
        os.makedirs(title)
    error_pic_urls = []
    success_pic_num = 0
    repeat_pic_num = 0
    index = 1
    for url in pic_urls:
        file_name = os.sep.join((title, basename(urlsplit(url)[2])))
        if os.path.exists(file_name):
            print('图片{}已存在'.format(file_name))
            index += 1
            repeat_pic_num += 1
            continue

        try:
            urllib.request.urlretrieve(url, file_name)
            success_pic_num += 1
            index += 1
            print('下载 {} 完成（{}/{}）'.format(file_name, index, len(pic_urls)))
        except:
            print('下载 {} 失败（{}/{}）'.format(file_name, index, len(pic_urls)))
            error_pic_urls.append(url)
            index += 1
            continue

    print('图片全部下载完毕!（成功：{}/重复：{}/失败：{}）'.format(success_pic_num, repeat_pic_num, len(error_pic_urls)))
    if len(error_pic_urls) > 0:
        print('下面打印失败的图片地址')
        for url in error_pic_urls:
            print(url)


if __name__ == '__main__':
    get_image_url()
