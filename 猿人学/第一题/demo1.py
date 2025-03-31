
import requests

import subprocess
from functools import partial  # 用来固定某个参数的固定值
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
# 解决execjs执行js时产生的乱码报错，需要在导入execjs模块之前，让Popen的encoding参数锁定为utf-8


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie": "sessionid=7l1wkuue0bhqf48pgpr6gc8hlrvipxy1"
}
url = "https://match.yuanrenxue.cn/api/match/1"


#
# response = requests.get(url, headers=headers, params=params)
#
# print(response.text)
# print(response)
s = 0   # 每一页的机票价格之和
times = 0   # 一共有多少次班机
for i in range(1, 6):
    f = open("demo.js", "r", encoding="utf-8")
    js_code = f.read()
    f.close()
    ctx = js_code = execjs.compile(js_code)
    verify_param = ctx.call("get_params")
    m = verify_param
    params={
        'page':i,
        'm':m
    }
    response = requests.get(url, params=params, headers=headers)
    json_data = response.json()
    print(json_data)

    s += sum([i.get("value") for i in json_data.get("data")])
    times += len(json_data.get("data"))
result = s // times     # 最终的结果，平均价格
print(result)   # 最终结果为4700