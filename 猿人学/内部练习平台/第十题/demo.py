import requests


headers = {
"Connection": "keep-alive",
"Content-Length": "6",
"sec-ch-ua": '"Not=A?Brand";v="99", "Chromium";v="118"',
"Accept": "application/json, text/javascript, */*; q=0.01",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"sec-ch-ua-mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
"sec-ch-ua-platform": "Windows",
"Origin": "https://www.python-spider.com",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://www.python-spider.com/challenge/10",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"

}
cookies = {
    "sessionid": "7pioxpbbrur6y62103z5hlegwyp318ya",
}
url = "https://www.python-spider.com/api/challenge10"
session =requests.session()
session.headers.clear()
session.headers.update(headers)


sum = 0
for i in range(1,101):
    data = {
        "page": "{}".format(i)
    }
    cookies = {
        "sessionid": "xm12q754jdxf3ijdyvkzrr4cpdqegrjn",
    }
    response = session.post(url, headers=headers, cookies=cookies, data=data)
    print(response.json())
    print("第{}页".format(i))
    Data = response.json()['data']
    for values in Data:
        sum+=int(values['value'].strip())
print(sum)