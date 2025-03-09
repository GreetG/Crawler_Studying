import json
import math
import random
import re
import time

import cv2
import ddddocr
import execjs
import numpy as np
import requests
from PIL import Image

obj = re.compile(r'geetest_.*?\((?P<json_date>.*)\)')
def handle_jsonp(s):
    text=obj.search(s).group('json_date')
    # return json.loads(text)
    return json.loads(text)
def download(url,save_path,session):
    img_response = session.get(url)
    with open(save_path,'wb') as f:
        f.write(img_response.content)
def restore_picture():
    img_list = ["./imgs/乱序缺口背景图.jpg", "./imgs/乱序背景图.jpg"]
    for index, img in enumerate(img_list):
        image = Image.open(img)
        s = Image.new("RGBA", (260, 160))
        ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42,
              12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
        height_half = 80
        for inx in range(52):
            c = ut[inx] % 26 * 12 + 1
            u = height_half if ut[inx] > 25 else 0
            l_ = image.crop(box=(c, u, c + 10, u + 80))
            s.paste(l_, box=(inx % 26 * 10, 80 if inx > 25 else 0))

        if index == 0:
            s.save("./imgs/修复缺口背景图片.png")

        else:
            s.save("./imgs/修复背景图片.png")
def cul_que():
    det = ddddocr.DdddOcr(show_ad=False,det=False,ocr=False)
    with open('./imgs/修复缺口背景图片.png','rb') as f:
        background_bytes =f.read()
    with open('./imgs/滑块图.png','rb') as f:
        target_bytes =f.read()
    res = det.slide_match(background_bytes=background_bytes,target_bytes=target_bytes,simple_target=True)
    return res['target'][0]
headers = {
    "authority": "demos.geetest.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://demos.geetest.com/slide-float.html",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
url = "https://demos.geetest.com/gt/register-slide"
t=time.time()
session = requests.Session()
params = {
    "t": f"{t}"
}
def get_gt_challenge(url,headers,params):
    response = session.get(url, headers=headers, params=params).json()
    gt=response['gt']
    challenge=response['challenge']
    return gt,challenge
f = open("jiyan.js","r",encoding="utf-8")
js_code = f.read()
f.close()
ctx = js_code = execjs.compile(js_code)
gt,challenge = get_gt_challenge(url,headers,params)
w1_key=ctx.call("get_first_w",gt,challenge)
















c_s_url = "https://api.geevisit.com/get.php"
params_get_c_s = {
    'is_next': 'true',
    'type': 'slide3',
    'gt': f'{gt}',
    'challenge': f'{challenge}',
    'lang': 'zh - cn',
    'https': 'true',
    'protocol': 'https: //',
    'offline': 'false',
    'product': 'embed',
    'api_server': 'api.geevisit.com',
    'isPC': 'true',
    'autoReset': 'true',
    'width': '100 %',
    'callback': 'geetest_1741509304334'
}
response = session.get(url=c_s_url, params=params_get_c_s)
c_s_result=handle_jsonp(response.text)
c=c_s_result['data']['c']
s=c_s_result['data']['s']
print(c_s_result)


step_2_url = "https://api.geevisit.com/ajax.php"
step_2_param={
    'gt': f'{gt}',
    'challenge': f'{challenge}',
    'lang': 'zh - cn',
    'pt': '0',
    'client_type': 'web',
    'w': "",
    'callback': 'geetest_1741513998331'
}
step2_request = session.get(url=step_2_url, params=step_2_param)
print(handle_jsonp(step2_request.text))

step_3_url = "https://api.geevisit.com/get.php"
step_3_param={
    'is_next': 'true',
    'type': 'slide3',
    'gt': f'{gt}',
    'challenge': f'{challenge}',
    'lang': 'zh-cn',
    'https': 'true',
    'protocol': 'https://',
    'offline': 'false',
    'product': 'embed',
    'api_server': 'api.geevisit.com',
    'isPC':'true',
    'autoReset': 'true',
    'width': '100%',
    'callback': 'geetest_1741512019950'
}
step3_request = session.get(url=step_3_url, params=step_3_param)
print(handle_jsonp(step3_request.text))



new_param_result = handle_jsonp(step3_request.text)


gt = new_param_result['gt']
challenge = new_param_result['challenge']
bg = new_param_result['bg']
fullbg = new_param_result['fullbg']
slice = new_param_result['slice']
c_sign = new_param_result['c']
s_sign = new_param_result['s']


bg_img_url = "https://static.geetest.com/"+bg
fg_img_url = "https://static.geetest.com/"+fullbg
slice_img_url = "https://static.geetest.com/"+slice
download(bg_img_url,"./imgs/乱序缺口背景图.jpg",session)
download(fg_img_url,"./imgs/乱序背景图.jpg",session)
download(slice_img_url,"./imgs/滑块图.png",session)
restore_picture()
distance =cul_que() + 6




# def get_slide_track(distance):
#     """
#     根据滑动距离生成滑动轨迹
#     :param distance: 需要滑动的距离
#     :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
#         x: 已滑动的横向距离
#         y: 已滑动的纵向距离, 除起点外, 均为0
#         t: 滑动过程消耗的时间, 单位: 毫秒
#     """
#
#     if not isinstance(distance, int) or distance < 0:
#         raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
#     # 初始化轨迹列表
#     slide_track = [
#         [random.randint(-50, -10), random.randint(-50, -10), 0],
#         [0, 0, 0],
#     ]
#     # 共记录count次滑块位置信息
#     count = 10 + int(distance / 2)
#     # 初始化滑动时间
#     t = random.randint(50, 100)
#     # 记录上一次滑动的距离
#     _x = 0
#     _y = 0
#     for i in range(count):
#         # 已滑动的横向距离
#         x = round(__ease_out_expo(i / count) * distance)
#         # y = round(__ease_out_expo(i / count) * 14)
#         # 滑动过程消耗的时间
#         t += random.randint(10, 50)
#         if x == _x:
#             continue
#         slide_track.append([x, _y, t])
#         _x = x
#     slide_track.append(slide_track[-1])
#     return slide_track, slide_track[-1][2]
# def get_trace_and_times(distance):
#     x = [0, 0]
#     y = [0, 0, 0]
#     z = [0]
#     count = np.linspace(-math.pi / 2, math.pi / 2, random.randrange(20, 30))
#     func = list(map(math.sin, count))
#     nx = [i + 1 for i in func]
#     add = random.randrange(10, 15)
#     sadd = distance + add
#     x.extend(list(map(lambda x: x * (sadd / 2), nx)))
#     x.extend(np.linspace(sadd, distance, 3 if add > 12 else 2))
#     x = [math.floor(i) for i in x]
#     for i in range(len(x) - 2):
#         if y[-1] < 30:
#             y.append(y[-1] + random.choice([0, 0, 1, 1, 2, 2, 1, 2, 0, 0, 3, 3]))
#         else:
#             y.append(y[-1] + random.choice([0, 0, -1, -1, -2, -2, -1, -2, 0, 0, -3, -3]))
#     for i in range(len(x) - 1):
#         z.append((z[-1] // 100 * 100) + 100 + random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]))
#     trace = list(map(list, zip(x, y, z)))
#     times = trace[-1][-1] + random.randint(1, 5)
#     return trace, times


import random


def __ease_out_expo(sep):
    '''
        轨迹相关操作
    '''
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)


def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 10 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # y = round(__ease_out_expo(i / count) * 14)
        # 滑动过程消耗的时间
        t += random.randint(10, 50)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track, slide_track[-1][2]



trace,passtime=get_slide_track(distance)

print(distance)


w=ctx.call("get_lastw",c,s,challenge,trace,gt,distance,passtime,w1_key[1])



callback = f'geetest_{int(time.time() * 1000)}'
#
finally_param={
'gt': f'{gt}',
'challenge': f'{challenge}',
'lang': 'zh-cn',
'$_BCN': '0',
'client_type': 'web',
   'w':f"{w}",
'callback': f'{callback}'
}


finally_url = 'https://api.geevisit.com/ajax.php'
finally_step_result = session.get(url=finally_url, params=finally_param)
print(finally_step_result.text)
# print(w)









