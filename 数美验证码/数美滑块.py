import json
import random
import execjs
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

def get_random(distance):
    """
    param
    	distance ： 缺口位置
   	return
    	track_list： 轨迹数组
    """

    #初始轨迹
    track_list = [[0,random.randint(-20,-2),0]]

    #随机记录滑动次数
    while True:
        before_track = track_list[-1]
        x = random.randint(0,40)
        y = 0
        z = random.randint(98,102)
        new_x = x + before_track[0]
        new_z = z + before_track[2]
        if new_x >= distance:
            track_list.append([distance, y, new_z])
            break
        else:
            track_list.append([new_x,y,new_z])

    for i in range(3):
        before_track = track_list[-1]
        z = random.randint(99, 101)
        track_list.append([before_track[0], before_track[1], z + before_track[2]])

    return track_list

def cul_que():
    det = ddddocr.DdddOcr(show_ad=False)
    with open('bg.jpg','rb') as f:
        background_bytes =f.read()
    with open('fg.jpg','rb') as f:
        target_bytes =f.read()
    res = det.slide_match(background_bytes,target_bytes,simple_target=True)
    return res['target'][0]

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
    "captchaUuid": "20250307022623mTWxDC3xi75pKKXy24",
    "rversion": "1.0.4",
    "callback": "sm_1741286645601",
    "channel": "DEFAULT"
}
session = requests.session()
response = session.get(url, headers=headers, params=params)

dict_jsonp = handle_jsonp(response.text)
fg_url="https://castatic.fengkongcloud.cn"+dict_jsonp['detail']['fg']
bg_url="https://castatic.fengkongcloud.cn"+dict_jsonp['detail']['bg']
rid=dict_jsonp['detail']['rid']

download(fg_url,'fg.jpg',session)
download(bg_url,'bg.jpg',session)

que=cul_que() // 2
gui = get_random(que)
f = open("demo1.js","r",encoding="utf-8")
js_code = f.read()
f.close()
ctx = js_code = execjs.compile(js_code)
verify_param=ctx.call("cul",que,gui,org,rid)
verify_url = "https://captcha1.fengkongcloud.cn/ca/v2/fverify"
verify_response = session.get(verify_url, params=verify_param)
print(verify_response.text)

