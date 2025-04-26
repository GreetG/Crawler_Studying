import hashlib

import requests

headers = {
    'authority': 'www.python-spider.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'sessionid=du3h4qm45dfd6al7b22d2tm7kofmqeb8; no-alert=true',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'referer': 'https://www.python-spider.com/challenge/58',
    'sec-ch-ua': '^\\^Not=A?Brand^\\^;v=^\\^99^\\^, ^\\^Chromium^\\^;v=^\\^118^\\^',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


sum = 0
session =requests.session()
for i in range(1,101):
    print(f"第{i}页")
    data = {
        'page': f'{i}',
        'token': '{}'.format(hashlib.md5(f'{i}'.encode()).hexdigest()[8:-8])
    }
    cookies = {
        "sessionid": "mdgzzgxgyse9effw34gzdg3bhlbi3x3u",
    }
    response = requests.post('https://www.python-spider.com/api/challenge58', headers=headers, cookies=cookies, data=data)
    print(response.json())
    for values in response.json()['data']:
        sum+=int(values['value'].strip())
print(sum)