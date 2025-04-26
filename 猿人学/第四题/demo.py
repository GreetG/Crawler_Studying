#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import time

import requests
import requests
# 隧道域名:端口号


headers = {
    "authority": "www.python-spider.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "referer": "https://www.python-spider.com/challenge/4",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
        "sessionid": "28igno1wqhfv40pt9nawufsqfps3yokr"
    }
target_url = "https://www.python-spider.com/api/challenge4"
sum = 0
for i in range(1,101):


    data = {
        "page": "{}".format(i)
    }
    proxies = {"http": "http://113.223.213.141:8089"}
    response = requests.post(target_url, headers=headers, cookies=cookies, data=data,proxies=proxies)
    print(response.json())
    print("第{}页".format(i))
    Data = response.json()['data']
    for values in Data:
        # print()
        sum+= int(values['value'].strip())
print(sum)
