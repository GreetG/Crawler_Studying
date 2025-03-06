import json
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # 新增导入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 配置浏览器选项
options = Options()
options.binary_location = r"C:\Users\10137\AppData\Local\CentBrowser\Application\chrome.exe"  # 浏览器路径
driver_path = r"C:\chromedriver\chromedriver.exe"  # 驱动路径

# 初始化驱动（关键修改部分）
service = Service(executable_path=driver_path)  # 使用 Service 对象
driver = webdriver.Chrome(service=service, options=options)

# 后续操作保持不变
driver.get("https://books.toscrape.com/")
driver.implicitly_wait(10)
all_data=driver.find_element(By.XPATH,value="//*[@id='default']/div/div/div/div/form/strong[1]").text
page=driver.find_element(By.XPATH,value="//*[@id='default']/div/div/div/div/form/strong[3]").text
all_page=eval(all_data)/eval(page)
for i in range(1,int(all_page+1)):
    driver.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    book_list=driver.find_elements(By.XPATH,"//*[@id='default']/div[1]/div/div/div/section/div[2]/ol/li")
    for book in book_list:
        All_book = []
        title=book.find_element(By.XPATH,"./article/h3/a")
        price=book.find_element(By.XPATH,"./article/div[2]/p[1]").text
        author=book.find_element(By.XPATH,"./article/h3/a").text
        title = title.get_attribute('title')
        All_book.append({
            "title":title,
            "price":price,
            "author":author
        })
        json.dump(All_book[0], open("books.json", "a"),indent=4)
driver.quit()
