import execjs
import requests


headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://match.yuanrenxue.cn/match/2",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
total = 0
for i in range(1,6):
    f = open("demojs.js", "r", encoding="utf-8")
    Cookies = f.read()
    f.close()
    js_code = execjs.compile(Cookies)

    m = js_code.call("get_params")

    cookies = {
        "sessionid": "u6dxe15dar303vnzsyv325ryl5sjcn4w",
        "m": m,

    }


    url = "https://match.yuanrenxue.cn/api/match/2"
    params = {
        "page": "{}".format(i)
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    values = response.json()['data']
    for value in values:
        total += value['value']
print(total)
# 5244
# 6841
# 7603
# 787
# 5533