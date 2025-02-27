import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
def getMaxNumber():
    url="https://www.ptt.cc/bbs/Stock/index.html"
    tree = etree.HTML(requests.get(url,headers=headers).text)
    max_number=tree.xpath("//*[@id='action-bar-container']/div/div[2]/a[2]/@href")[0]
    max_number=max_number.replace("/bbs/Stock/index","")
    max_number = max_number.replace(".html", "")
    return eval(max_number)

def getPageUrl(max_number):

    for i in range(int(max_number),1,-1 ):
        url = f"https://www.ptt.cc/bbs/Stock/index{i}.html"
        tree = etree.HTML(requests.get(url,headers=headers).text)
        page_urls = tree.xpath("//*[@class='r-ent']/div[2]/a/@href")
        for page_url in page_urls:
            page_url = "https://www.ptt.cc" + page_url
            data=getPageContent(page_url)
            with open("output.txt", "a", encoding="utf-8") as f:
                for key, value in data.items():
                    f.write(f"{key}:{value}\n")
            print(f"写入第{i}篇")


def getPageContent(page_url):

    tree = etree.HTML(requests.get(page_url,headers=headers).text)
    author_info = tree.xpath("//*[@id='main-content']/div[1]")
    author = author_info[0].xpath("./span[1]/text()")
    name = author_info[0].xpath("./span[2]/text()")
    author = author+name
    author = ''.join(author)


    title_info = tree.xpath("//*[@id='main-content']/div[3]")
    title_tag = title_info[0].xpath("./span[1]/text()")
    title = title_info[0].xpath("./span[2]/text()")
    title = title_tag+title
    title = ''.join(title)

    time_info = tree.xpath("//*[@id='main-content']/div[4]")
    time_tag = time_info[0].xpath("./span[1]/text()")
    time = time_info[0].xpath("./span[2]/text()")
    time = time_tag+time
    time = ''.join(time)

    content =tree.xpath("//*[@id='main-content']/text()")
    content = [re.sub(r'\s+', '', item) for item in content]
    content=''.join(content)

    data = {'author':author,'title':title,'time':time,'content':content}
    return data

if __name__ == '__main__':
    Maxnumber=getMaxNumber()
    page_url=getPageUrl(Maxnumber)

