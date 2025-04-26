import execjs
import requests
import json


f = open("demo.js","r",encoding="utf-8")
js_code = f.read()
f.close()
ctx = js_code = execjs.compile(js_code)

verify_headers=ctx.call("get_header")
headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Tingyun": f"{verify_headers[3]}",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-tif-nonce": f"{verify_headers[1]}",
    "x-tif-paasid": "undefined",
    "x-tif-signature": f"{verify_headers[2]}",
    "x-tif-timestamp": f"{verify_headers[0]}"
}

url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
verify_data = ctx.call("get_param")

data = {
    "data": {
        "data": {
            "encData": f"{verify_data[1]}"
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": 1744861435,
        "signData": f"{verify_data[0]}"
    }
}
cookies = {
    "acw_tc": "3ccdc15817448613941915859e444e33786d8fbdd60a563c804f6b55174fa4",
    "gb_nthl_sessionId": "b53475a8478a481c9082ff2253e4c783",
    "yb_header_show": "true"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data,cookies=cookies)
print(response.text)
print(response)


