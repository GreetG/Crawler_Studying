import requests



headers = {

"Connection": "keep-alive",
"sec-ch-ua": '"Not=A?Brand";v="99", "Chromium";v="118"',
"sec-ch-ua-mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
"sec-ch-ua-platform": "Windows",
"Accept": "*/*",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://stu.tulingpyton.cn/problem-detail/2/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"


}
cookies = {
    "sessionid": "ji2p4auw6ddty3ksce9jy5eo4j15v06t",
    "Hm_lvt_b5d072258d61ab3cd6a9d485aac7f183": "1744347075,1744354800",
    "HMACCOUNT": "AC20A32F15E2F278",
    "Hm_lpvt_b5d072258d61ab3cd6a9d485aac7f183": "1744355056"
}
url = "https://stu.tulingpyton.cn/api/problem-detail/2/data/"
sum = 0
for i in range(1,21):
    params = {
        "page": "{}".format(i)
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    Values = response.json()['current_array']
    print("第{}页".format(i))
    print(Values)
    for value in Values:
        sum+=value
print(sum)