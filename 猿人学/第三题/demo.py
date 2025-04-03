from curl_cffi import requests
headers1 = {
    'Connection': 'keep-alive',
    'Content-Length': 0,
    'sec-ch-ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': "Windows",
    'Accept': '*/*',
    'Origin: https':'//match.yuanrenxue.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
headers2 = {
    'sec-ch-ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
   ' X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
   ' User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',

}

cookies = {
    "sessionid": "da9jows627tky71djg971msz6q2r2xls",
}
url = "https://match.yuanrenxue.cn/api/match/3"
params = {
    "page": "2"
}
s = requests.Session()
s.post("https://match.yuanrenxue.cn/jssm", headers=headers1, cookies=cookies)
response = s.get(url, headers=headers2, cookies=cookies, params=params)

print(response.text)
print(response)