import json

import execjs
import requests

headers = {
    'authority': 'www.python-spider.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1745149010; HMACCOUNT=B703310BCB27C76C; sessionid=1ky4jd6lcka7yjn6wgo8b72cpe3ntr5f; no-alert=true; m=155; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1745152061',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'referer': 'https://www.python-spider.com/challenge/55',
    'sec-ch-ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


sum = 0
for i in range(1,101):
    data = {
        'page': f'{i}'
    }

    response = requests.post('https://www.python-spider.com/api/challenge55', headers=headers, data=data)
    decode_result = response.json()["result"]
    with open("demo.js","r",encoding="utf")as f:
        jscode = f.read()
        ctx = execjs.compile(jscode)
        encode_result = ctx.call("decode", decode_result)
        encode_result=json.loads(encode_result)
        print(encode_result)
        for data in encode_result['data']:
            sum += int(data['value'])
print(sum)