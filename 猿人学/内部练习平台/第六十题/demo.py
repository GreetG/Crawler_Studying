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
    "referer": "https://www.python-spider.com/challenge/60",
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
    "no-alert": "true",
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1744813045",
    "HMACCOUNT": "12380A4F235AC9A2",
    "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1744813896"
}
sum = 0
for i in range(1,101):
    print(f"第{i}页")
    f = open("demo.js", "r", encoding="utf-8")
    cryptourl = f.read()
    f.close()
    js_code = execjs.compile(cryptourl)
    cryptourl = js_code.call("get_crypto_url", i)
    url = f"https://www.python-spider.com/api/challenge60/{cryptourl}"
    data = {
        "page": f"{i}"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    all_data = response.json()
    print(all_data)
    for data in all_data["data"]:
        sum+= int(data["value"])
print(sum)