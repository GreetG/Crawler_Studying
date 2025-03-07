# 数美滑块逆向分析  
*** 
本项目主要难点在于分析传入的js包,解析里面的加密参数找出加密方法和图片距离与滑动轨迹
***

*第一步就是解析js包发现主要的有两个，一个验证，一个生成图片*
*首先可通过获取curl直接生成request发现生成图片的请求没有动态的参数因此可直接获取图片并进行解析*
```
obj = re.compile(r'sm_.*?\((?P<json_date>.*)\)')
def handle_jsonp(s):
    text=obj.search(s).group('json_date')
    return json.loads(text)
def download(url,save_path,session):
    img_response = session.get(url)
    with open(save_path,'wb') as f:
        f.write(img_response.content)
```  
*在返回的数据中是使用jsonp，需要使用正则和json模块来进行处理*  

*随后是分析加密参数，参数主要分成两部分加密，分析过程中发现是用extend进行合并的，跟栈可以找到合并部分，打上断点分析可以知道一部分是通过鼠标轨迹进行加密，一部分是使用固定值进行加密，可以将加密方法获取下来或者通过python模拟*
```
function getEncryptContent(data,key){
    key = CryptoJS.enc.Utf8.parse(key)
    data = process_type(data)
    var encrypted =CryptoJS.DES.encrypt(data,key,{
        iv:"",
        mode:CryptoJS.mode.ECB,
        padding:CryptoJS.pad.ZeroPadding

    });
    return encrypted.toString();

}
```
*其中需要注意的就是数据处理部分，这部分我写的不是特别好就不拿出来讲了，需要注意的就是数字和string字符串的处理，我是通过一个个比对才发现出的问题，有时候字符串的引号被传进去加密了，这可能也是一个小的易错点把*

*最后也就是模式匹配和轨迹算法了，这里我是先后用了ddddocr和opencv这两种,感觉都还行,但ddddocr毕竟是训练后的模型效果还是很可以的*
```
def get_distance(fg, bg):
    fg_image = np.asarray(bytearray(requests.get(url=fg, verify=False).content), dtype='uint8')
    fg_image = cv2.imdecode(fg_image, 1)
    shape = fg_image.shape
    x_points, y_points = [], []
    for x_point in range(shape[0]):
        for y_point in range(shape[1]):
            if list(fg_image[x_point][y_point]) != [0, 0, 0]:
                x_points.append(x_point)
                y_points.append(y_point)
    fg_cut_image = fg_image[min(x_points):max(x_points), ]

    bg_image = np.asarray(bytearray(requests.get(url=bg, verify=False).content), dtype='uint8')
    bg_image = cv2.imdecode(bg_image, 1)
    bg_cut_image = bg_image[min(x_points):max(x_points), ]

    result = cv2.matchTemplate(bg_cut_image, fg_cut_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    distance = max_loc[0]
    return int(distance)
```
*finally就是传参数进去检验啦，值得注意的就是图片大小和检验大小这块，网站上显示大小只有二分之一*  
![结果展示](https://github.com/GreetG/Crawler_Studying/blob/d44e44dc029aef9261342337a219fe5cd27cf19e/imgs/%E6%A0%91%E8%8E%93%E6%BB%91%E5%9D%97.png)  
