import json

import execjs
import requests


headers = {
    "authority": "www.python-spider.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "referer": "https://www.python-spider.com/challenge/57",
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
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1744383597,1744472984,1744529852,1744639178",
    "HMACCOUNT": "FDFCADBBC1BB025A",
    "sessionid": "h4ubnr8l2tp6k05q2nxx18mpjhhr39zh",
    "no-alert": "true",
    "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1744643582"
}
url = "https://www.python-spider.com/api/challenge57"
sum = 0
session =requests.session()
for i in range(1,101):
    print(f"第{i}页")
    data = {
        "page": "{}".format(i)
    }
    cookies = {
        "sessionid": "mdgzzgxgyse9effw34gzdg3bhlbi3x3u",
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    f = open("demo2.js", "r", encoding="utf-8")
    Cookies = f.read()
    f.close()
    js_code = execjs.compile(Cookies)
    crypt_result = response.json()['result']
    m = js_code.call("get_result", crypt_result)
    m = json.loads(m)
    print(m)
    for values in m['data']:
        sum+=int(values['value'].strip())
print(sum)


