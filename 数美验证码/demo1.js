//npm install crypto-js

var CryptoJS = require("crypto-js")
function process_type(data){
    if (typeof data == "number"){
        console.log(data)
        return data + ""
    }else{
        return JSON.stringify(data)
    }

}
function cul(hen,gui,org,rid){
    var _0x23447b = {}

    var gui = [[],[],[]]
    var end_point = gui[gui.length-1]
    var diff_tm = end_point[end_point.length - 1] - 0 + 31;
    console.log(diff_tm)
    testtm=[
    [0, 4, 0],
    [13, 0, 102],
    [43, -2, 201]
]
    // _0x23447b['tb'] = getEncryptContent(hen / 300, '59fcff86');
    _0x23447b['tb'] = getEncryptContent(0.14666666666666667, '59fcff86');
    _0x23447b['tm'] = getEncryptContent(testtm, '0569c403');
    // _0x23447b['ly'] = getEncryptContent(diff_tm, '65986a6b');
    _0x23447b['ly'] = getEncryptContent(238, '65986a6b');
    _0x23447b['fc'] = getEncryptContent(300, 'f1553d1a');
    _0x23447b['uc'] = getEncryptContent(150, 'b0f132ec');
    _0x23447b['act.os'] = 'web_pc';
    _0x23447b['og'] = getEncryptContent(1, "aa3146c6");
    _0x23447b['jp'] = getEncryptContent(0, "8584558c");
    _0x23447b['aj'] = getEncryptContent(-1, "b295ccbf");





    _0x23447b['sy'] = getEncryptContent("default", "7d9ab4ed");
    _0x23447b['wz'] = getEncryptContent2("'DEFAULT'", "4a61a388");


    _0x23447b['dj'] = getEncryptContent("zh-cn", "566e29c3");
    _0x23447b['gp'] = getEncryptContent("11", "5300a156");
    _0x23447b['rid'] = rid
    _0x23447b["rversion"] = "1.0.4"
    _0x23447b['sdkver'] = "1.1.3"
    _0x23447b['protocol'] = "184"
    _0x23447b['ostype'] = "web"
    _0x23447b['organization'] = org
    _0x23447b["callback"]="sm_1741286645601"

    return _0x23447b;
}
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
function getEncryptContent2(data,key){
    key = CryptoJS.enc.Utf8.parse(key)
    var encrypted =CryptoJS.DES.encrypt(data,key,{
        iv:"",
        mode:CryptoJS.mode.ECB,
        padding:CryptoJS.pad.ZeroPadding

    });
    return encrypted.toString();

}

// cul()

