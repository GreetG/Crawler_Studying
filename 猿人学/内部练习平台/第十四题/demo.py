import execjs
import requests

with open("demo.js","r",encoding="utf-8") as file:
    jscode = file.read()
    js_code = execjs.compile(jscode)


sum = 0
for i in range(1,101):
    ctx = js_code.call("get_param", i)
    data = {
        "page":f"{i}",
        "uc":ctx
    }

    resp=requests.post("https://www.python-spider.com/api/challenge14",data=data)
    print(resp.json()['data'])
    for data in resp.json()['data']:
        sum+=int(data['value'])
print(sum)