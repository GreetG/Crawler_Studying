import csv
import json
import re
import time

import curl_cffi
import execjs
import pandas as pd
from fake_useragent import UserAgent

# 创建UserAgent对象
ua = UserAgent()

# 获取随机浏览器UA
random_ua = ua.random
df = pd.read_excel("usps_input.xlsx", engine="openpyxl")
column_values = df['USPS_Number'].to_numpy()
for column in column_values:
    time.sleep(3)
    data = {
        "direct_trackings":[
            {"tracking_number":f"{column}","additional_fields":{},"slug":""}
        ],
        "translate_to":"en"
    }
    data_str = json.dumps(data, separators=(",", ":"))  # 关键参数：去掉多余空格
    with open("demo.js","r",encoding="utf-8") as file:
        jscode = file.read()
        jscode = re.sub(r"___jscode___",data_str,jscode)
        ctx = execjs.compile(jscode)
        headers_param =ctx.call("get_header")
    signature = headers_param[0]
    am_sign_time = headers_param[1]
    digest = headers_param[2]
    headers = {
        'authority': 'track.aftership.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'am-sign-time': f'{am_sign_time}',
        'am-sign-version': 'v1',
        'authorization': f'hmac username="track.aftership.com", algorithm="hmac-sha256", headers="digest", signature="{signature}"',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'digest': f'{digest}',
        'origin': 'https://www.aftership.com',
        'pragma': 'no-cache',
        'referer': 'https://www.aftership.com/',
        'user-agent': random_ua,
        'visitor-id': '8274533072568241',#这个设置成自定义的
    }
    response = curl_cffi.post('https://track.aftership.com/api/v2/direct-trackings/batch', headers=headers, data=data_str,impersonate="chrome124")
    order_status=response.json()['data']['direct_trackings'][0]['tracking']['latest_status']
    print("订单号" + column + "状态" + order_status)
    header = ["USPS_Number", "Status"]
    with open("usps_output.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:  # 文件为空时写入表头
            writer.writerow(header)
        writer.writerow(
            [
                column,
                order_status
            ]
        )
