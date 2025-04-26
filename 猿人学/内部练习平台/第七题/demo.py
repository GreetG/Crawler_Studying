import requests


headers = {
    "authority": "www.python-spider.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "referer": "https://www.python-spider.com/challenge/7",
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
    "sessionid": "mdgzzgxgyse9effw34gzdg3bhlbi3x3u",
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1744353275,1744353933",
    "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1744353933",
    "HMACCOUNT": "AC20A32F15E2F278"
}
url = "https://www.python-spider.com/api/challenge7"
session =requests.session()
sum = 0
for i in range(1,101):
    data = {
        "page": "{}".format(i)
    }
    cookies = {
        "sessionid": "mdgzzgxgyse9effw34gzdg3bhlbi3x3u",
        "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1744353275,1744353933",
        "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1744353933",
        "HMACCOUNT": "AC20A32F15E2F278"
    }
    step1 = session.get("https://www.python-spider.com/cityjson", headers=headers, cookies=cookies)
    response = session.post(url, headers=headers, cookies=cookies, data=data)
    print(response.json())
    print("第{}页".format(i))
    Data = response.json()['data']
    for values in Data:
        # print()
        sum+= int(values['value'].strip())
print(sum)