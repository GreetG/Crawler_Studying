# 国家医保
# 医保服务平台SM国密逆向分析

# 声明

本文章中所有内容仅供学习交流，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！
***
这个项目难点在于解析网站headers与plylod中的参数加密
***
*首先是header参数加密，通过获取curl并调试可以发现X-Tingyun，x-tif-nonce，x-tif-signature，x-tif-timestamp均被加密，可直接搜索发现加密逻辑*  
```
s = Math.ceil((new Date).getTime() / 1e3),
    h = i123(),
    f = s + h + s;
    var w = CryptoJS.SHA256(f).toString();
    testkey = '4Nl_NnGbjwY';
    var x = ";x=" + Ir(), i = "c=B|" + testkey;
    XTingyun=i + x
```
***给对应的参数打上断点发现w参数是通过sha256进行加密，可直接使用cryptojs进行模拟*** 

*然后是payload参数加密signData和encData，这里sm2没进行修改可直接模拟，但sm4进行了魔改需要进方法扣js进行还原，注意参数a中的d不能直接在源码里面拿需要在运行中获取，且为定值* 
```
        var n = m(t)
        , i = p(n);
    // console.log(t)
        i.data = p(i.data);
        var r = v(i)
        , a = sm2.doSignature(r, "009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42", {
        hash: !0
        });
        // console.log(a)
        sign_DATA =  Buffer.from(a, "hex").toString("base64")
        
        
        
    var  n123  =JSON.stringify(t.data)
    // console.log(n123)
    var a = A(n123);
        console.log(a)
    var u = l.appCode
    // console.log(u)

    var s = y(u, "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P")
    // console.log(s)
    var l = b(s, a);
        // console.log(l)
        enc_DATA = l.toUpperCase()
```
***将header和payload都逆向模拟出来后可直接发送请求获取数据，注意timestamp需要保持一致***

***最后是解密环节，搜索encData找到send函数一路追踪发现解密逻辑***
```
function get_response(q){
            var n = Buffer.from(q, "hex")
              , i = function(t, n) {
                var i = m_finally(n, t)
                  , r = i[i.length - 1];
                return i = i.slice(0, i.length - r),
                Buffer.from(i).toString("utf-8")
            }(y_test("T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ", "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P"), n);
            return JSON.parse(i)
        }
```
***这里需要注意，直接从接口获取的encData会带个\n换行不知道会不会有影响，并且直接用execjs会报错编码问题，需要调用以下函数***

```
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
```
***并且需要修改subprocess里面的encoding，改成utf-8***
*代码不可直接运行，已对b函数进行修改*


![结果展示](https://github.com/GreetG/Crawler_Studying/blob/e675b49f89c89b02f85112b5ad7c918ea35018b3/imgs/%E5%8C%BB%E4%BF%9D.png)  
