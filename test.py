from curl_cffi import requests
from fake_useragent import UserAgent

ua = UserAgent()

# 获取随机浏览器UA


def check_tls_fingerprint():
    url = "https://tls.peet.ws/api/all"
    ua_list = ["edge99",
               "edge101",
               "chrome99",
               "chrome100",
               "chrome101",
               "chrome104",
               "chrome107",
               "chrome110",
               "chrome116",
               "chrome119",
               "chrome120",
               "chrome123",
               "chrome124",
               "chrome131",
               "chrome133a",
               "chrome99_android",
               "chrome131_android",
               # Safari
               "safari15_3",
               "safari15_5",
               "safari17_0",
               "safari17_2_ios",
               "safari18_0",
               "safari18_0_ios",
               # Firefox
               "firefox133",
               "firefox135",
               "chrome",
               "edge",
               "safari",
               "safari_ios",
               "chrome_android",
               "firefox"
               ]

    for browser in ua_list:
        try:
            headers = {'User-Agent': ua.random}
            resp = requests.get(url, impersonate=browser,headers=headers)
            print(f"\n--- {browser} ---")
            print(resp.json())  # 输出 TLS/HTTP2 信息
        except Exception as e:
            print(f"Failed for {browser}: {e}")


check_tls_fingerprint()