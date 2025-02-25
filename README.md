# Python爬虫自学  
*** 
这是一个简单的验证码破解流程，通过获取验证码url，导入函数库tesseract并调用里面的image_to_string方法将简单的验证码识别出来，通过破解验证码实现一般网站的登录自动化 
***
*识别的重点在于将图像进行灰度和二值化处理*  

```
def preprocess_image(self, image):
image = image.convert('L')  # 转为灰度
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2)  # 增强对比度
image = image.point(lambda x: 0 if x < 180 else 255)  # 二值化
return image
```  

***最后将识别的结果存入data中并发送请求***