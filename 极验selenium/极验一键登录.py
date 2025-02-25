import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # 新增导入
from selenium.webdriver.common.by import By

# 配置浏览器选项
options = Options()
options.binary_location = r"C:\Users\10137\AppData\Local\CentBrowser\Application\chrome.exe"  # 浏览器路径
driver_path = r"C:\chromedriver\chromedriver.exe"  # 驱动路径

# 初始化驱动（关键修改部分）
service = Service(executable_path=driver_path)  # 使用 Service 对象
driver = webdriver.Chrome(service=service, options=options)

# 后续操作保持不变
driver.get("https://demos.geetest.com/fullpage.html")
time.sleep(5)
test=driver.find_element(by=By.ID,value="captcha")
ActionChains(driver).click(test).perform()
time.sleep(5)
submit=driver.find_element(by=By.ID,value="btn")
ActionChains(driver).click(submit).perform()
time.sleep(5)
driver.quit()