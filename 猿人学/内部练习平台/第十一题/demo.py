import re

import execjs
import requests


headers = {
    "authority": "www.python-spider.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.python-spider.com/challenge/11",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


cookies = {
    "sessionid": "923gbg1fdzijbetjvtjmrzc1v1o577c8",
}
url = "https://www.python-spider.com/challenge/11"

response = requests.get(url, headers=headers, cookies=cookies)
jscode = re.match("<script>(.*)</script>",response.text).group(1)
with open("deno.js", "r", encoding="utf-8") as f:
    jslcode=f.read().replace("__jscode",jscode)
    jslcode=execjs.compile(jslcode).call("get_cookie")
    f.close()

jslcode = jslcode.split("=")[1].split(";")[0]
cookies = {
    "sessionid": "923gbg1fdzijbetjvtjmrzc1v1o577c8",
    "__jsl_clearance":f"{jslcode}"
}
response = requests.get(url, headers=headers, cookies=cookies)
pattern = r'<td class="info">\s*(\d+)\s*<\/td>'
matches = re.findall(pattern, response.text)
sum = 0
for match in matches:
    sum = sum + int(match)
print(sum)