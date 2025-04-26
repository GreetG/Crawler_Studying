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
    "referer": "https://www.python-spider.com/challenge/56",
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
    "sessionid": "heir23byynl32mhqwvrqgn55lyvopl7e",
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1744986311",
    "HMACCOUNT": "10BAEF5A4F52D03D",
    "iloveu": "9a6700592c0beb9fb82995681b6c98448488f72f",
    "yuanrenxue34": "wdu9WnEj3a",
    "no-alert": "true",
    "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1744990251"
}
url = "https://www.python-spider.com/api/challenge56"
sum = 0
for i in range(1,101):
    data = {
        "page": f"{i}"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    result_decrypto = response.json()['result']
    with open("demo.js","r",encoding="utf-8") as file:
        jscode = file.read()
    compiled_code = execjs.compile(jscode)
    ctx = compiled_code.call("get_result",1,result_decrypto)
    print(ctx)
    for data in ctx:
        sum+=int(data['value'])
print(sum)