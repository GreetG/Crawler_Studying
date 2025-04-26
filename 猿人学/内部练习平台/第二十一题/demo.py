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
    "referer": "https://www.python-spider.com/challenge/59",
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
    "sessionid": "x4xtjlpopku7764t0379qy8o14mr0rj1",
}
url = "https://www.python-spider.com/api/challenge21"
sum = 0
for i in range(1, 101):
    with open("demo.js", "r", encoding="utf-8") as f:
        jscode = f.read()
        js_code = execjs.compile(jscode)
        ctx = js_code.call("test")
    s = ctx[0]
    t = ctx[1]
    data = {
        "page": f"{i}",
        "s":s,
        "t":t
    }
    print(f"第{i}页")
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(response.json())
    for data in response.json()['data']:
        sum += int(data['value'])
print(sum)