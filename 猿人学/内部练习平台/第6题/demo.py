import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.python-spider.com",
    "Pragma": "no-cache",
    "Referer": "https://www.python-spider.com/challenge/6",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.python-spider.com/api/challenge6"
sum = 0
session =requests.session()
for i in range(1,101):
    data = {
        "page": "{}".format(i)
    }
    cookies = {
        "sessionid": "mdgzzgxgyse9effw34gzdg3bhlbi3x3u",
        "no-alert": "true"
    }
    response = session.post(url, headers=headers, cookies=cookies, data=data)
    print(response.json())
    print("第{}页".format(i))
    Data = response.json()['data']
    for values in Data:
        sum+=int(values['value'].strip())
print(sum)