import curl_cffi


headers = {
    "authority": "www.python-spider.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "referer": "https://www.python-spider.com/challenge/24",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "65zd0y30qk295pqwujz2jzybkpbxm92f",
    "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1744639178,1744875384,1744899002,1744986066",
    "HMACCOUNT": "FDFCADBBC1BB025A",
    "no-alert": "true",
    "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1744986081"
}
url = "https://www.python-spider.com/api/challenge24"
sum=0
for i in range(1,101):
    data = {
        "page": f"{i}"
    }
    response = curl_cffi.post(url, headers=headers, cookies=cookies, data=data)

    datavalue=response.json()['data']
    for data in datavalue:
        sum+=int(data['value'])
print(sum)