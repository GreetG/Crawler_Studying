import re

import requests

headers = {
    'authority': 'www.python-spider.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1745238243; HMACCOUNT=E836D67AB037E31F; sessionid=1xrnvedjyp6z9py91adm0tweltn8cwry; no-alert=true; __yr_token__=b301cDDcFHkEDWnYJfgc9WwcYamYgWh9oa3lgU0dbW312L2p7T1d6MH57dAN7ZSEeTB4BICYJPldXVlEnd2sFXV5zaB8bG0MvAB5oOjc0LU10SEYvbygbJkE0WAZYF3ZrXAZPABUMG3kJWQNBYRY=; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1745247079',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'referer': 'https://www.python-spider.com/challenge/12',
    'sec-ch-ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


font={
    "&#xf712":"0",
    "&#xe458":"1",
    "&#xf375":'2',
    "&#xf80c":'3',
    "&#xf12f":'4',
    "&#xee4a":'5',
    "&#xf295":'6',
    "&#xe449" : '7',
    "&#xf0d6":'8',
    "&#xe44d":'9'
}
sum = 0
for i in range(1,101):
    data = {
      'page': f'{i}'
    }
    response = requests.post('https://www.python-spider.com/api/challenge12', headers=headers, data=data)
    # print(response.json()['data'])
    for data in response.json()['data']:
        result=data['value']
        result = re.sub(
            r"&#x[0-9a-fA-F]+",
            lambda m: font[m.group()],
            result
        ).replace(" ", "")

        # 2. 转为整数（可选）
        result = int(result)
        print(result)
        sum +=result
print(sum)