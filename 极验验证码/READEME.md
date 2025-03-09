# 极验滑块逆向分析  
*** 
本项目主要难点在于分析传入的js包,解析里面的加密参数找出加密方法和图片距离与滑动轨迹
***

*第一步就是解析js包发现主要的有register-slide,get.php,ajax.php*
*首先可通过获取curl直接生成request,获取gt和challenge*
```
def get_gt_challenge(url,headers,params):
    response = session.get(url, headers=headers, params=params).json()
    gt=response['gt']
    challenge=response['challenge']
    return gt,challenge
f = open("jiyan.js","r",encoding="utf-8")
js_code = f.read()
f.close()
ctx = js_code = execjs.compile(js_code)
gt,challenge = get_gt_challenge(url,headers,params)
w1_key=ctx.call("get_first_w",gt,challenge)
```  
*搜索w参数可直接进栈，发现w是i和r相加生成的继续分析i和r的逻辑，key是生成的16位字符串，四次相加的结果，对象o是进行了AES加密随后在进行base64编码，我这里还原了aes加密具体如下*  
```
function get_key() {
    let data = ""
    for (let i = 0; i<4;i++){
        data  = data + (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1)

    }
    return data

}
function Aes_encrypt(text, key_value) {
    var key = CryptoJS.enc.Utf8.parse(key_value);
    var iv = CryptoJS.enc.Utf8.parse("0000000000000000");
    var srcs = CryptoJS.enc.Utf8.parse(text);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    for (var r = encrypted, o = r.ciphertext.words, i = r.ciphertext.sigBytes, s = [], a = 0; a < i; a++) {
        var c = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s.push(c);
    }
    return s;
}
    var r = new H()['encrypt'](key);
    var o = Aes_encrypt(JSON['stringify'](config), key)
    var i = me['$_BEHm'](o)
    var w1 = i + r
```
*在获取第一个w后可以带这gt,challenge,w对ajax发送请求获取如下*  
{'status': 'success', 'data': {'result': 'slide'}}
*随后可以带这gt,challenge,w对get.php发送请求获取如下* 
```
{'gt': '019924a82c70bb123aae90d483087f94', 'challenge': 'b1c226707df7f42197f4c67281b283386y', 'id': 'ab1c226707df7f42197f4c67281b28338', 'bg': 'pictures/gt/7bfaaa72b/bg/cf6be3dfa.jpg', 'fullbg': 'pictures/gt/7bfaaa72b/7bfaaa72b.jpg', 'link': '', 'ypos': 23, 'xpos': 0, 'height': 160, 'slice': 'pictures/gt/7bfaaa72b/slice/cf6be3dfa.png', 'api_server': 'https://api.geevisit.com/', 'static_servers': ['static.geetest.com/', 'static.geevisit.com/'], 'mobile': True, 'theme': 'ant', 'theme_version': '1.2.6', 'template': '', 'logo': True, 'clean': False, 'type': 'multilink', 'fullpage': False, 'feedback': 'https://www.geetest.com/contact#report', 'show_delay': 250, 'hide_delay': 800, 'benchmark': False, 'version': '6.0.9', 'product': 'embed', 'https': True, 'width': '100%', 'show_voice': True, 'c': [12, 58, 98, 36, 43, 95, 62, 15, 12], 's': '455f6646', 'so': 0, 'i18n_labels': {'cancel': '取消', 'close': '关闭验证', 'error': '请重试', 'fail': '请正确拼合图像', 'feedback': '帮助反馈', 'forbidden': '怪物吃了拼图，请重试', 'loading': '加载中...', 'logo': '由极验提供技术支持', 'read_reversed': False, 'refresh': '刷新验证', 'slide': '拖动滑块完成拼图', 'success': 'sec 秒的速度超过 score% 的用户', 'tip': '请完成下方验证', 'voice': '视觉障碍'}, 'gct_path': '/static/js/gct.b71a9027509bc6bcfef9fc6a196424f5.js'}
```
*在这里可以注意到challenge发送改变由32位变成34位，s值也发生改变* 
*最后解析验证包直接搜索，发现w是由h+u生成的,详细代码如下* 
```
        var o ={
            "lang": "zh-cn",
            "userresponse": H2(distance, challenge),
            "passtime": time,
            "imgload": 52,
                "aa":W['prototype']['$_BBED'](W['prototype']['$_FD_'](trace), c, s),
            "ep": {
                "v": "7.9.2",
                "$_BIE": false,
                "me": true,
                "tm": {
                    "a": 1741466135364,
                    "b": 1741466135408,
                    "c": 1741466135408,
                    "d": 0,
                    "e": 0,
                    "f": 1741466135365,
                    "g": 1741466135365,
                    "h": 1741466135365,
                    "i": 1741466135365,
                    "j": 1741466135365,
                    "k": 0,
                    "l": 1741466135368,
                    "m": 1741466135399,
                    "n": 1741466135403,
                    "o": 1741466135409,
                    "p": 1741466135521,
                    "q": 1741466135521,
                    "r": 1741466135522,
                    "s": 1741466135523,
                    "t": 1741466135523,
                    "u": 1741466135523
                },
                "td": -1
            },
            "h9s9": "1816378497",
            "rp": CryptoJS.MD5(gt_param + old_challenge + time).toString()
        }
        l = V['encrypt'](gt['stringify'](o), key)
        var u =new U()['encrypt'](key)
        h = m['$_FEX'](l)
        w = h + u
```

*其中需要注意的就是rp中的challenge是32位的*

*最后也就是模式匹配和轨迹算法了，在第二次请求获取新的challenge时也将fg和bg，slice发送了过来，可以直接获取*

*可以发现图片被处理过是乱码情况，需要对canvas进行解析，这里是用python直接进行还原*
```
def download(url,save_path,session):
    img_response = session.get(url)
    with open(save_path,'wb') as f:
        f.write(img_response.content)
def restore_picture():
    img_list = ["./imgs/乱序缺口背景图.jpg", "./imgs/乱序背景图.jpg"]
    for index, img in enumerate(img_list):
        image = Image.open(img)
        s = Image.new("RGBA", (260, 160))
        ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42,
              12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
        height_half = 80
        for inx in range(52):
            c = ut[inx] % 26 * 12 + 1
            u = height_half if ut[inx] > 25 else 0
            l_ = image.crop(box=(c, u, c + 10, u + 80))
            s.paste(l_, box=(inx % 26 * 10, 80 if inx > 25 else 0))

        if index == 0:
            s.save("./imgs/修复缺口背景图片.png")

        else:
            s.save("./imgs/修复背景图片.png")
```
*获取了完整的图片和滑块图片就可以计算距离，生成轨迹，和passtime滑动时间，这里使用了ddddocr进行模式匹配，然后手调了一些距离*
```

def cul_que():
    det = ddddocr.DdddOcr(show_ad=False,det=False,ocr=False)
    with open('./imgs/修复缺口背景图片.png','rb') as f:
        background_bytes =f.read()
    with open('./imgs/滑块图.png','rb') as f:
        target_bytes =f.read()
    res = det.slide_match(background_bytes=background_bytes,target_bytes=target_bytes,simple_target=True)
    return res['target'][0]
distance =cul_que() + 6
def __ease_out_expo(sep):
    '''
        轨迹相关操作
    '''
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)


def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 10 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # y = round(__ease_out_expo(i / count) * 14)
        # 滑动过程消耗的时间
        t += random.randint(10, 50)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track, slide_track[-1][2]



trace,passtime=get_slide_track(distance)
```
*finally就是传参数进去检验啦，这里是通过了参数，但轨迹这一块被阻挡了，这轨迹是真的难啊*  
