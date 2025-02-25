# 极验一键登录  
*** 
本项目主要难点在于基础的selenium的实现对于相应元素的定位与基础的selenium操作
***

*实现的重点在与通过开发者工具找到对应元素通过find_element定位元素，并通过Auction函数快捷实现浏览器操作*

```
//将目标网址传入get函数
driver.get("https://demos.geetest.com/fullpage.html")
time.sleep(5)
//定位验证按钮
test=driver.find_element(by=By.ID,value="captcha")
ActionChains(driver).click(test).perform()
time.sleep(5)
//定位登录按钮
submit=driver.find_element(by=By.ID,value="btn")
ActionChains(driver).click(submit).perform()
time.sleep(5)

driver.quit()
```  
*selenium的缺陷就是需要设置一些sleep来等待网页渲染*