import requests
import curl_cffi
headers = {
    'authority': 'www.python-spider.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1745238243; HMACCOUNT=E836D67AB037E31F; sessionid=1xrnvedjyp6z9py91adm0tweltn8cwry; no-alert=true; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1745241608; __yr_token__=b301cDH9mPGsuaRFgYn89VWQFeVVscjQxZ0YRBUFnOCBHEGgGT1d6MH57dFc6RFYeZBB8Gh9AOQhADVB/FlsrH2JzaB8bG0NSAiFZZ1QIKxsFd0p2RABXFVIpWAZYF3ZrXAZPABUMG3kJWQNBYRY=',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'referer': 'https://www.python-spider.com/challenge/22',
    'sec-ch-ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
sum = 0
for i in range(1,101):
    data = {
      'page': f'{i}'
    }
    cookies = {
        "sessionid": "x4xtjlpopku7764t0379qy8o14mr0rj1",
        '__yr_token__': 'b301cDCB8PzFvYnRLPxhRR1UoVxYKfSZgcVFrVy1mVEAFEyxxT1d6Qnt0dAwvTCAeZHsqeikpV2BdNTwEbxNEAWtzaB8bG0MlRiIbBzgJR0l/YFwnVg8xVnwEWAZYF3ZrXAZPABUMG3kJWQNBYRY=',
    }
    response = curl_cffi.post('https://www.python-spider.com/api/challenge29', headers=headers, data=data,impersonate="Chrome101",cookies=cookies)
    print(response.json()['data'])
    for data in response.json()['data']:
        sum += int(data['value'])
print(sum)