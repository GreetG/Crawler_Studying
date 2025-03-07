import json
import math
import random

import cv2
import execjs
import numpy as np
import requests
import re
import ddddocr
obj = re.compile(r'sm_.*?\((?P<json_date>.*)\)')
def handle_jsonp(s):
    text=obj.search(s).group('json_date')
    return json.loads(text)
def download(url,save_path,session):
    img_response = session.get(url)
    with open(save_path,'wb') as f:
        f.write(img_response.content)
def get_distance(fg, bg):
    fg_image = np.asarray(bytearray(requests.get(url=fg, verify=False).content), dtype='uint8')
    fg_image = cv2.imdecode(fg_image, 1)
    shape = fg_image.shape
    x_points, y_points = [], []
    for x_point in range(shape[0]):
        for y_point in range(shape[1]):
            if list(fg_image[x_point][y_point]) != [0, 0, 0]:
                x_points.append(x_point)
                y_points.append(y_point)
    fg_cut_image = fg_image[min(x_points):max(x_points), ]

    bg_image = np.asarray(bytearray(requests.get(url=bg, verify=False).content), dtype='uint8')
    bg_image = cv2.imdecode(bg_image, 1)
    bg_cut_image = bg_image[min(x_points):max(x_points), ]

    result = cv2.matchTemplate(bg_cut_image, fg_cut_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    distance = max_loc[0]
    return int(distance)
def cul_que():
    det = ddddocr.DdddOcr(show_ad=False,det=False,ocr=False)
    with open('bg.jpg','rb') as f:
        background_bytes =f.read()
    with open('fg.jpg','rb') as f:
        target_bytes =f.read()
    res = det.slide_match(background_bytes=background_bytes,target_bytes=target_bytes,simple_target=True)
    return res['target'][0]/2
def get_trace_and_times(distance):
    x = [0, 0]
    y = [0, 0, 0]
    z = [0]
    count = np.linspace(-math.pi / 2, math.pi / 2, random.randrange(20, 30))
    func = list(map(math.sin, count))
    nx = [i + 1 for i in func]
    add = random.randrange(10, 15)
    sadd = distance + add
    x.extend(list(map(lambda x: x * (sadd / 2), nx)))
    x.extend(np.linspace(sadd, distance, 3 if add > 12 else 2))
    x = [math.floor(i) for i in x]
    for i in range(len(x) - 2):
        if y[-1] < 30:
            y.append(y[-1] + random.choice([0, 0, 1, 1, 2, 2, 1, 2, 0, 0, 3, 3]))
        else:
            y.append(y[-1] + random.choice([0, 0, -1, -1, -2, -2, -1, -2, 0, 0, -3, -3]))
    for i in range(len(x) - 1):
        z.append((z[-1] // 100 * 100) + 100 + random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]))
    trace = list(map(list, zip(x, y, z)))
    times = trace[-1][-1] + random.randint(1, 5)
    return trace, times
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.ishumei.com",
    "Pragma": "no-cache",
    "Referer": "https://www.ishumei.com/trial/captcha.html",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://captcha1.fengkongcloud.cn/ca/v1/register"
org = "d6tpAY1oV0Kv5jRSgxQr"
params = {
    "lang": "zh-cn",
    "model": "slide",
    "data": "{}",
    "organization": org,
    "sdkver": "1.1.3",
    "appId": "default",
    "captchaUuid": "20250307052547MZa6fp5ySkhr6JRrxE",
    "rversion": "1.0.4",
    "callback": "sm_1741299467338",
    "channel": "DEFAULT"
}
session = requests.session()
response = session.get(url, headers=headers, params=params)
dict_jsonp = handle_jsonp(response.text)
fg_url="https://castatic.fengkongcloud.cn"+dict_jsonp['detail']['fg']
bg_url="https://castatic.fengkongcloud.cn"+dict_jsonp['detail']['bg']
rid=dict_jsonp['detail']['rid']
que=get_distance(fg_url,bg_url)

trace,time = get_trace_and_times(que/2)
f = open("demo1.js","r",encoding="utf-8")
js_code = f.read()
f.close()
ctx = js_code = execjs.compile(js_code)
verify_param=ctx.call("cul",que/2,trace,org,rid,time)
verify_url = "https://captcha1.fengkongcloud.cn/ca/v2/fverify"
verify_response = session.get(verify_url, params=verify_param)

print(verify_response.text)