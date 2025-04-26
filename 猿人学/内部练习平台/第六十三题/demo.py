import requests
import execjs
import base64
import json

with open('demo.js', 'r', encoding="utf-8") as f:
    js_code = f.read()
js_ctx = execjs.compile(js_code)

sum = 0

for i in range(100):
    headers = {
        "authority": "www.python-spider.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"",
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.238.400 QQBrowser/12.4.5622.400",
        "sec-ch-ua-platform": "\"Windows\"",
        "origin": "https://www.python-spider.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.python-spider.com/challenge/63",
        "accept-language": "zh-CN,zh;q=0.9"
    }
    cookies = {
        "sessionid": "x4xtjlpopku7764t0379qy8o14mr0rj1",
    }
    url = "https://www.python-spider.com/api/challenge63"

    data = js_ctx.call("get_code", str(i + 1))

    response = requests.get(url, headers=headers, cookies=cookies, data=base64.b64decode(data))

    print(js_ctx.call("decode", base64.b64encode(response.content).decode('utf-8')))

    jsData = json.loads(js_ctx.call("decode", base64.b64encode(response.content).decode('utf-8')))

    for i in jsData['data']:
        print(i['value'])
        sum += int(i['value'])

    print(sum)
