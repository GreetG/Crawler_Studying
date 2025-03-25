# 猿人学第一题  
*** 
这道题主要难点在于对于oo0O0函数的格式化，然后找出window.f的生成逻辑
***
*最终m生成结果为*
```
function get_params() {
    var date = Date.parse(new Date()) + (16798545 + -72936737 + 156138192);
    window.f = hex_md5(date.toString())
    var result = window.f + '丨' + date / (-1 * 3483 + -9059 + 13542);
    return result
}
```

