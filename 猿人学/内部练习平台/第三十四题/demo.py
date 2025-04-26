import json

import requests
import execjs
import re
from lxml import etree

session = requests.session()
cookie = {
    "sessionid": "65zd0y30qk295pqwujz2jzybkpbxm92f",
}
_headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

session.cookies.update(cookie)
response = session.post(f"https://www.python-spider.com/challenge/34",headers=_headers)
pattern = r'<script type="text/javascript">(.*?)<\/script><script type="text/javascript">sEnc\(\);<\/script>'

match = re.search(pattern, response.text, re.DOTALL)
jscode = match.group(1)
cookie_str = "; ".join([f"{key}={value}" for key, value in session.cookies.items()])




with open("demo.js","r",encoding="utf-8") as f:
    js_code = f.read()
    compile = execjs.compile(js_code)
    iove_cookies_str = compile.call("decypt",cookie_str,jscode)
    print(iove_cookies_str)
    iove_cookies = {}
    for each in iove_cookies_str.split(";"):
        iove_cookies[each.split("=")[0]] = each.split("=")[1]
    session.cookies.update(iove_cookies)
print(session.cookies)
response = session.post(f"https://www.python-spider.com/challenge/34",headers=_headers)
print(response.text)
html = etree.HTML(response.text)
values = html.xpath("//tr/td/text()")
sum = 0
for value in values:
    sum = sum + int(value)
print(sum)
