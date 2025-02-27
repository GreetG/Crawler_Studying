# 台湾股票bbs论坛
***
这个项目难点在于解析网站翻页逻辑与ip问题，通过解析页面提取目标数据
***
*最新页面是在maxnumber的页面中，识别逻辑后通过组合生成url定位目标页面*  
```
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
```
***最后将识别的结果存入data中并保存为文本数据***  
![结果展示](..%2Fimgs%2Ftaiwanbbs.png)
